# Nama File : ServerGOT.py
# Programmer : 
    #   Yansen Dwi Putra (13220056)
    #   Bostang Palaguna (13220055)
# Tanggal : 
    # Minggu, 2 Juni 2024
    # Selasa, 4 Juni 2024

# Import Library
from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse
import threading
import socket
import logging
import ast
import json
from constant import *

server_ip = "10.8.102.118"


logging.basicConfig(
    filename='server.log',        # Nama file log
    level=logging.DEBUG,          # Level log
    format='%(asctime)s %(levelname)s %(message)s'  # Format log
)

# Data pengguna
data = [
    {'id': 1, 'username': 'yansen','password':'phoenix' , 'coin': 30},
    {'id': 2, 'username': 'bostang','password':'tes' , 'coin': 20},
    {'id': 3, 'username': 'kunga','password':'tes' , 'coin': 10},
    {'id': 4, 'username': 'lord','password':'tes' , 'coin': 9999},
    {'id': 5, 'username': 'newbie','password':'tes' , 'coin': 0},
]

def write_to_json_file(filename, data):
    # Menulis data ke file JSON
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def read_from_json_file(filename):
    # Membaca data dari file JSON
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

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
    return response
            
def validation(username, password,id):
    data = read_from_json_file('database.json')
    # print("Data from JSON file:", data)  # Debugging statement
    for user in data:
        if user['username'] == username and user['password'] == password and id == id_login:
            return True, user['id']
        elif user['username'] == username and id == id_register:
            return True, user['id']
            
    return False, user['id']    

def run_http_server():
    server_address = (server_ip, 8080)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
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

write_to_json_file('database.json', data)

# print(data)
http_thread.start()
socket_thread.start()
http_thread.join()
socket_thread.join()
