# Nama File : ServerGOT.py
# Programmer : 
    #   Yansen Dwi Putra (13220056)
    #   Bostang Palaguna (13220055)
# Tanggal : 
    # Minggu, 2 Juni 2024
    # Selasa, 4 Juni 2024

# Import Library
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import urllib.parse
import threading
import socket
import logging
import ast
import json
from datetime import datetime
from constant import *

server_ip = "10.8.105.201"
matchmaking = [[0, 0]]
rooms = []   # [room_id, player1_id, player2_id, action1, action2]



logging.basicConfig(
    filename='server.log',        # Nama file log
    level=logging.DEBUG,          # Level log
    format='%(asctime)s %(levelname)s %(message)s'  # Format log
)

# Data pengguna
# data = [
#     {'id': 1, 'username': 'yansen','password':'phoenix' , 'coin': 30},
#     {'id': 2, 'username': 'bostang','password':'tes' , 'coin': 20},
#     {'id': 3, 'username': 'kunga','password':'tes' , 'coin': 10},
#     {'id': 4, 'username': 'lord','password':'tes' , 'coin': 9999},
#     {'id': 5, 'username': 'newbie','password':'tes' , 'coin': 0},
# ]

def write_to_json_file(filename, data):
    # Menulis data ke file JSON
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def read_from_json_file(filename):
    # Membaca data dari file JSON
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def get_outcome(player1_decision, player2_decision):
    if player1_decision == COOPERATE and player2_decision == COOPERATE:
        return (DRAW_POINT, DRAW_POINT)  # Both cooperate
    elif player1_decision == COOPERATE and player2_decision == CHEAT:
        return (LOSE_POINT, WIN_POINT)  # Player 1 cooperates, Player 2 cheats
    elif player1_decision == CHEAT and player2_decision == COOPERATE:
        return (WIN_POINT, LOSE_POINT)  # Player 1 cheats, Player 2 cooperates
    elif player1_decision == CHEAT and player2_decision == CHEAT:
        return (LOSE_POINT, LOSE_POINT)  # Both cheat

def get_id(username):
    data = read_from_json_file('database.json')
    for user in data:
        if user['username'] == username:
            return user['id']
    return 0

def create_room(player1_id, player2_id):  # Membuat room. Return room_id dan array room yang ditambahkan
    room_id = f"{player1_id:0>3}{player2_id:0>3}"
    rooms.append([room_id, player1_id, player2_id, 0, 0])

def remove_room(room_id): # Menghapus room dengan room_id. Return array room yang sudah diubah
    updated_array = [item for item in rooms if item[0] != room_id]
    return updated_array

def find_room(room_id):   # Mencari index dari room dengan room_id. Return -1 jika tidak ditemukan
    for i, room in enumerate(rooms):
        if room[0] == room_id:
            return i
    return -1

def find_room_id(id):
    for room in rooms:
        if room[1] == id:
            return room[0]
        if room[2] == id:
            return room[0]
    return -1

def validation(username, password,id):
    data = read_from_json_file('database.json')
    # print("Data from JSON file:", data)  # Debugging statement
    for user in data:
        if user['username'] == username and user['password'] == password and id == id_login:
            return True, user['id']
        elif user['username'] == username and id == id_register:
            return True, user['id']
            
    return False, user['id'] 

# Setup Server HTTP
class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):

        logging.info('Received GET request')
        # Parsing path dan query
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        user_data = query.get('data', [''])[0]
        user_data_list = user_data.split(',')
        user_data_list = ast.literal_eval(user_data)
        if not isinstance(user_data_list, list):
            raise ValueError
        # print(int(user_data_list[0]))
        response = logic(user_data_list)
            # leaderboard
        logging.info(f'Received data: {user_data}')
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response.encode())
        
def logic(user_data_list):
    msg_id = int(user_data_list[0])   
    #######################################
    #######  request untuk LOGIN   ########
    ####################################### 
    if msg_id == id_login:
        username = user_data_list[1]
        password = user_data_list[2]
        is_valid, user_id = validation(username, password, msg_id)
        response = f'{is_valid}'
        if is_valid:
            print("Autentikasi berhasil")
        else:
            print("Autentikasi gagal")

    #######################################
    #######  request untuk REGISTER #######
    ####################################### 
    elif msg_id == id_register:
        username = user_data_list[1]
        password = user_data_list[2]
        is_valid, user_id = validation(username, password, msg_id)
        response = f"{is_valid}"
        if is_valid:
            print("Nama pengguna-kata sandi sudah digunakan")
            # response = f'hello, username: {username} and password: {password} already been used'
        else:
            data = read_from_json_file('database.json')
            for user in data:
                biggest = 0
                if user['id'] > biggest:
                    biggest = user['id']
            append_data = {'id':biggest+1,'username':username,'password':password,'coin':0}
            data.append(append_data)
            write_to_json_file('database.json', data)
            print("Nama pengguna-kata sandi berhasil ditambahkan")
    #######################################
    ###### request untuk LEADERBOARD ######
    ####################################### 
    elif msg_id == id_leaderboard_request: 
        username = user_data_list[1]
        data = read_from_json_file('database.json')
        sorted_data = sorted(data, key=lambda x: x["coin"], reverse=True)[:10]
        leaderboard = [[item['username'], item['coin']] for item in sorted_data]
        i = 0
        username_coin = 0
        for user in sorted_data:
            i += 1
            if user["username"] == username:
                username_coin = user["coin"]
                ranking = i
        player_leaderboard = [username,ranking,username_coin]
        response = f'{id_register},{leaderboard},{player_leaderboard}'
    #######################################
    ###### request untuk JOIN ROOM   ######
    #######################################
    # format resquest :[id,matchmaking_id]

    elif msg_id == id_room_join:   # room join
        username = user_data_list[1]
        id = get_id(username)
        opponent = user_data_list[2]
        print("msg_id = ", msg_id, ", id = ", id, ", opponent = ", opponent) # Debugging untuk melihat input 
        print(matchmaking)  # Debugging untuk melihat array matchmaking

        if opponent == "": # Random Matchmaking
            
            if matchmaking[0][0] != 0: # Jika ada pemain lain yang masuk random matchmaking
                matchmaking[0][1] = id  # Tambahkan id supaya diketahui check pemain satu lagi
                response = f'{True}'    # Memberikan room_id
            else:
                matchmaking[0][0] = id  # Tambah request

                # Menunggu request pemain lain sampai timeout/ditemukan
                match_found = False
                start_time = datetime.now()
                while (datetime.now() - start_time).seconds <= timeout and not match_found:
                    if matchmaking[0][1] != 0:
                        match_found = True

                if not match_found:
                    response = f'{False}'    # Memberitahukan pemain bahwa request timeout
                else:
                    create_room(matchmaking[0][0], matchmaking[0][1]) # Memberikan room_id dan room
                    response = f'{True}'

                matchmaking[0] = [0, 0] # Reset random matchmaking
        
        else:   # Targeted matchmaking
            # Melihat jika pemain lain telah membuat request matchmaking
            matchmaking_id = get_id(username)

            match_found1 = False
            for matchmaking_room in matchmaking:
                if (matchmaking_room[0] == matchmaking_id):
                    matchmaking_room[1] = id    # Tambahkan id supaya diketahui check pemain satu lagi
                    match_found1 = True
                    break

            print("match found1 = ", match_found1)# Debugging untuk melihat jika pemain lain telah membuat request matchmaking

            if match_found1:    # Sudah ada
                response = f'{True}'  # Memberikan room_id

            else:   # Belum ada
                matchmaking.append([id, 0]) # Tambah request
                
                # Menunggu request pemain lain sampai timeout/ditemukan
                match_found2 = False
                start_time = datetime.now() 
                while (datetime.now() - start_time).seconds <= timeout and not match_found2:
                    for matchmaking_room in matchmaking:
                        if matchmaking_room[0] == id and matchmaking_room[1] != 0:
                            matchmaking_room[1] = matchmaking_id    
                            match_found2 = True

                if (not match_found2):
                    response = f'{False}'  # Memberitahukan pemain bahwa request timeout
                else:
                    create_room(matchmaking[0][0], matchmaking[0][1]) # Memberikan room_id dan room
                    response = f'{True}'

                matchmaking[:] = [matchmaking_room for matchmaking_room in matchmaking if matchmaking_room[0] != id]    # Menghapus request matchmaking karena timeout

    #######################################
    ###### request untuk MATCH START ######
    #######################################
    elif msg_id == id_match_start:   # match start
        
        player_username = user_data_list[1]
        player_id = get_id(player_username)
        action = int(user_data_list[2])
        room_id = find_room_id(player_id)

        room_index = find_room(room_id)   # Mendapatkan index room dengan room_id

        error_check = False # Variabel untuk menyimpan jika terjadi error

        if (room_index == -1):
            response = f"Room dengan room_id:{room_id} tidak ditemukan!"

        else:
            if (rooms[room_index][1] == player_id):  # Jika id yang diberikan player 1
                if (rooms[room_index][3] != 0):
                    response = f"Sudah memberikan input!"
                    error_check = True
                else:
                    player_no = 1   # Variabel untuk melihat player ke berapa
                    rooms[room_index][3] = action
                    # print(f"Player input {rooms[room_index][3]}")   # Debugging input player 1
                
            elif (rooms[room_index][2] == player_id):  # Jika id yang diberikan player 2
                if (rooms[room_index][4] != 0):
                    response = f"Sudah memberikan input!"
                    error_check = True
                else:
                    player_no = 2   # Variabel untuk melihat player ke berapa
                    rooms[room_index][4] = action
                    # print(f"Player input {rooms[room_index][4]}")   # Debugging input player 2
                
            else:
                response = f"Id yang diberikan tidak valid"
                error_check = True

            if (error_check == False):   # Jika tidak terjadi error pada tahap sebelumnya
                
                # print(rooms)    # Debugging rooms
                
                if ((rooms[room_index][3] != 0) and (rooms[room_index][4] != 0)): # Pemain satu lagi sudah memberikan aksi
                    result1, result2 = get_outcome(rooms[room_index][3], rooms[room_index][4])    # Kalkulasi hasil

                    # Mengumumkan hasil dengan memeriksa pemain ke berapa
                    if (player_no == 1):
                        response = f"[{result1},{result2}]"

                    elif (player_no == 2):
                        response = f"[{result2},{result1}]"

                    else:
                        response = f"Terdapat error di server"
                        print("Error!! player_no tidak valid")

                else:
                    while (1):  # Menunggu pemain satu lagi
                        room_index = find_room(room_id)   # Mendapatkan index room dengan room_id
                        if ((rooms[room_index][3] != 0) and (rooms[room_index][4] != 0)): # Jika semua pemain sudah memberikan aksi
                            result1, result2 = get_outcome(rooms[room_index][3], rooms[room_index][4])    # Kalkulasi hasil
                            
                            remove_room(room_id)  # Menghilangkan room
                            print(rooms)

                            # Mengumumkan hasil dengan memeriksa pemain ke berapa
                            if (player_no == 1):
                                response = f"[{result1},{result2}]"
                                break

                            elif (player_no == 2):
                                response = f"[{result2},{result1}]"
                                break

                            else:
                                response = f"Terdapat error di server"
                                print("Error!! player_no tidak valid")
                                break
    return response   

def run_http_server():
    server_address = (server_ip, 8080)
    httpd = ThreadingHTTPServer(server_address, MyHTTPRequestHandler)
    print('HTTP server running on port 8080')
    httpd.serve_forever()

# Setup Server Socket
def run_socket_server():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, 65432))
    server_socket.listen(2)  # Listen for up to 2 connections
    print('Socket server running on port 65432')
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f'Connected by {addr}')
        logging.info(f'Connected by {addr}')
        data = client_socket.recv(1024)
        data_str = data.decode()
        data_list = data_str.split(',')
        # data_list = eval(data_str)
        response = logic(data_list).encode()
        if data:
            print('Received data:', data.decode())
            logging.info(f'Received data: {data.decode()}')
        client_socket.sendall(response)
        client_socket.close()

# Menjalankan kedua server secara bersamaan
http_thread = threading.Thread(target=run_http_server)
socket_thread = threading.Thread(target=run_socket_server)

# write_to_json_file('database.json', data)

# print(data)
http_thread.start()
socket_thread.start()
http_thread.join()
socket_thread.join()
