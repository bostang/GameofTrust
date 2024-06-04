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

room = [["001002", 1, 2, 0, 0]]   # [room_id, player1_id, player2_id, action1, action2]

logging.basicConfig(
    filename='server.log',        
    level=logging.DEBUG,          
    format='%(asctime)s %(levelname)s %(message)s'  
)

data = [
    {'id': 1, 'username': 'yansen', 'password': 'phoenix', 'coin': 30},
    {'id': 2, 'username': 'bostang', 'password': 'tes', 'coin': 20},
    {'id': 3, 'username': 'kunga', 'password': 'tes', 'coin': 10},
    {'id': 4, 'username': 'lord', 'password': 'tes', 'coin': 9999},
    {'id': 5, 'username': 'newbie', 'password': 'tes', 'coin': 0},
    {'id': 6, 'username': 'bostang', 'password': 'tes', 'coin': 5},
    {'id': 7, 'username': 'bostang', 'password': 'tes', 'coin': 9},
]

def write_to_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def read_from_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.info('Received GET request')
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        user_data = query.get('data', [''])[0]
        user_data_list = user_data.split(',')
        user_data_list = ast.literal_eval(user_data)
        if not isinstance(user_data_list, list):
            raise ValueError
        msg_id = int(user_data_list[0])
        
        #######################################
        #######  request untuk LOGIN   ########
        ####################################### 
        # format resquest :[id,username,password]
        # contoh :[1,abc,123]
        
        if msg_id == id_login: 
            username = user_data_list[1]
            password = user_data_list[2]
            is_valid, user_id = validation(username, password, msg_id)
            if is_valid:
                response = f'hello user {user_id}: {username}'
            else:
                response = f'hello, username: {username} and password: {password} already been used'
                
        #######################################
        #######  request untuk REGISTER #######
        ####################################### 
        # format resquest :[id,username,password]
        # contoh :[12,abc,123]

        elif msg_id == id_register:
            username = user_data_list[1]
            password = user_data_list[2]
            is_valid, user_id = validation(username, password, msg_id)
            if is_valid:
                response = f'hello, username: {username} and password: {password} already been used'
            else:
                data = read_from_json_file('database.json')
                biggest = max(user['id'] for user in data)
                append_data = {'id': biggest + 1, 'username': username, 'password': password, 'coin': 0}
                data.append(append_data)
                write_to_json_file('database.json', data)
                response = f'hello, username: {username} and password: {password} already been added'
                
        #######################################
        ###### request untuk LEADERBOARD ######
        #######################################
        # format resquest :[id,[leaderboard],[player_leaderboard]]
        # contoh :[2,abc,123]
        elif msg_id == id_leaderboard_request:
            username = user_data_list[1]
            data = read_from_json_file('database.json')
            sorted_data = sorted(data, key=lambda x: x["coin"], reverse=True)[:10]
            leaderboard = [[item['username'], item['coin']] for item in sorted_data]
            ranking = next((i for i, user in enumerate(sorted_data, 1) if user["username"] == username), 0)
            username_coin = next((user["coin"] for user in sorted_data if user["username"] == username), 0)
            player_leaderboard = [username, username_coin, ranking]
            response = f'{id_leaderboard_request},{leaderboard},{player_leaderboard}'

        #######################################
        ###### request untuk JOIN ROOM   ######
        #######################################
        # format resquest :[id,matchmaking_id]

        elif msg_id == id_room_join:   # room join
            id = int(user_data_list[1])
            matchmaking_id = int(user_data_list[2])
            print("msg_id = ", msg_id, ", id = ", id, ", matchmaking_id = ", matchmaking_id) # Debugging untuk melihat input 
            print(matchmaking)  # Debugging untuk melihat array matchmaking

            if matchmaking_id == 0: # Random Matchmaking
                
                if matchmaking[0][0] != 0: # Jika ada pemain lain yang masuk random matchmaking
                    matchmaking[0][1] = id  # Tambahkan id supaya diketahui check pemain satu lagi
                    response = f"{matchmaking[0][0]:0>3}{matchmaking[0][1]:0>3}"    # Memberikan room_id
                else:
                    matchmaking[0][0] = id  # Tambah request

                    # Menunggu request pemain lain sampai timeout/ditemukan
                    match_found = False
                    start_time = datetime.now()
                    while (datetime.now() - start_time).seconds <= timeout and not match_found:
                        if matchmaking[0][1] != 0:
                            match_found = True

                    if not match_found:
                        response = f'Timeout, other player not found'    # Memberitahukan pemain bahwa request timeout
                    else:
                        response, room = create_room(matchmaking[0][0], matchmaking[0][1], room) # Memberikan room_id dan room

                    matchmaking[0] = [0, 0] # Reset random matchmaking
            
            else:   # Targeted matchmaking
                # Melihat jika pemain lain telah membuat request matchmaking
                match_found1 = False
                for matchmaking_room in matchmaking:
                    if (matchmaking_room[0] == matchmaking_id):
                        matchmaking_room[1] = id    # Tambahkan id supaya diketahui check pemain satu lagi
                        match_found1 = True
                        break

                print("match found1 = ", match_found1)# Debugging untuk melihat jika pemain lain telah membuat request matchmaking

                if match_found1:    # Sudah ada
                    response = f"{matchmaking_id:0>3}{id:0>3}"  # Memberikan room_id

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

                    if not match_found2:
                        response = f'Timeout, other player not found'    # Memberitahukan pemain bahwa request timeout
                    else:
                        response, room = create_room(id, matchmaking_id, room)    # Memberikan room_id dan room

                    matchmaking[:] = [matchmaking_room for matchmaking_room in matchmaking if matchmaking_room[0] != id]    # Menghapus request matchmaking karena timeout
        
        #######################################
        ###### request untuk MATCH START ######
        #######################################
        elif msg_id == id_match_start:   # match start
            print(room)
            player_id = int(user_data_list[1])
            room_id = user_data_list[2]
            action = int(user_data_list[3])

            room_index = find_room(room_id, room)   # Mendapatkan index room dengan room_id

            error_check = False # Variabel untuk menyimpan jika terjadi error

            if (room_index):
                response = f"Room dengan room_id:{room_id} tidak ditemukan!"

            else:
                if (room[room_index][1] == player_id):  # Jika id yang diberikan player 1
                    if (room[room_index][3] == 0):
                        response = f"Sudah memberikan input!"
                        error_check = True
                    else:
                        player_no = 1   # Variabel untuk melihat player ke berapa
                        room[room_index][3] = action
                    
                elif (room[room_index][2] == player_id):  # Jika id yang diberikan player 2
                    if (room[room_index][4] == 0):
                        response = f"Sudah memberikan input!"
                        error_check = True
                    else:
                        player_no = 2   # Variabel untuk melihat player ke berapa
                        room[room_index][4] = action
                    
                else:
                    response = f"Id yang diberikan tidak valid"
                    error_check = True

                if (error_check == True):   # Jika tidak terjadi error pada tahap sebelumnya
                    while (1):
                        if ((room[room_index][3] != 0) and (room[room_index][4] != 0)): # Jika semua pemain sudah memberikan aksi
                            result1, result2 = get_outcome(room[room_index][3], room[room_index][4])    # Kalkulasi hasil
                            
                            # Mengumumkan hasil dengan memeriksa pemain ke berapa
                            if (player_no == 1):
                                response = f"Kamu mendapatkan {result1} poin, pemain lain mendapatkan {result2}"
                                break

                            elif (player_no == 2):
                                response = f"Kamu mendapatkan {result2} poin, pemain lain mendapatkan {result1}"
                                break

                            else:
                                response = f"Terdapat error di server"
                                print("Error!! player_no tidak valid")
                                break

        logging.info(f'Received data: {user_data}')
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response.encode())

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

def create_room(player1_id, player2_id, room):  # Membuat room. Return room_id dan array room yang ditambahkan
    room_id = f"{player1_id:0>3}{player2_id:0>3}"
    room.append([room_id, player1_id, player2_id, 0, 0])

    return room_id, room

def remove_room(room_id, room): # Menghapus room dengan room_id. Return array room yang sudah diubah
    updated_array = [item for item in room if item[0] != room_id]
    return updated_array

def find_room(room_id, room):   # Mencari index dari room dengan room_id. Return -1 jika tidak ditemukan
    for r in range(len(room)):
        if (r[0] == room_id):
            return r
    return -1

def validation(username, password, id):
    data = read_from_json_file('database.json')
    for user in data:
        if user['username'] == username and user['password'] == password and id == id_login:
            return True, user['id']
        elif user['username'] == username and id == id_register:
            return True, user['id']
    return False, user['id']

def run_http_server():
    server_address = (server_ip, 8080)
    httpd = ThreadingHTTPServer(server_address, MyHTTPRequestHandler)
    print('HTTP server running on port 8080')
    httpd.serve_forever()

def run_socket_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, 65432))
    server_socket.listen(2)
    print('Socket server running on port 65432')
    while True:
        client_socket, addr = server_socket.accept()
        print(f'Connected by {addr}')
        logging.info(f'Connected by {addr}')
        data = client_socket.recv(1024)
        if data:
            print('Received data:', data.decode())
            logging.info(f'Received data: {data.decode()}')
        client_socket.sendall(b'Hello from Socket server!')
        client_socket.close()

http_thread = threading.Thread(target=run_http_server)
socket_thread = threading.Thread(target=run_socket_server)

write_to_json_file('database.json', data)

http_thread.start()
socket_thread.start()
http_thread.join()
socket_thread.join()
