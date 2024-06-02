from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse
import threading
import socket
import logging
import ast
import json
server_ip = "10.8.103.141"


logging.basicConfig(
    filename='server.log',        # Log file name
    level=logging.DEBUG,          # Log level
    format='%(asctime)s %(levelname)s %(message)s'  # Log format
)

data = [
    {'id': 1, 'username': 'yansen','password':'phoenix' , 'coin': 30}
]
def write_to_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def read_from_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# HTTP Server setup
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
        print(int(user_data_list[0]))
        msg_id = int(user_data_list[0])
        # user_id = validation(username, password)
        username = user_data_list[1]
        password = user_data_list[2]
        is_valid, user_id = validation(username, password)
        print(is_valid)
        if msg_id == 1: #login request
            # username = user_data_list[1]
            # password = user_data_list[2]
            if is_valid:
                print("Authentication successful")
                response = f'hello user {user_id}: {username}'
                
            else:
                # response = f'hello, username: {username} and password: {password} already been used'
                print("Authentication failed")
            # while (validation(user_data_list[1],user_data_list[2])):
            #     print("error")
            # username = user_data_list[1]
            # print('username:',username)
            # password = user_data_list[2]
            # print('password:',password)
            
        elif msg_id == 12: #sign in request
            # username = user_data_list[1]
            # password = user_data_list[2]
            if is_valid:
                print("Username-password sudah digunakan")
                response = f'hello, username: {username} and password: {password} already been used'
            else:
                data = read_from_json_file('database.json')
                for user in data:
                    biggest = 0
                    if user['id'] > biggest:
                        biggest = user['id']
                append_data = {'id':biggest+1,'username':username,'password':password,'coin':0}
                data.append(append_data)
                write_to_json_file('database.json', data)
                print("Username-password berhasil ditambahkan")
                response = f'hello, username: {username} and password: {password} already been added'
        elif msg_id == 2: #leaderboard request
            username = user_data_list[1]
            data = read_from_json_file('database.json')
            leaderboard = []
            while len(leaderboard) <= 10:   
                biggest = 0 
                biggest_id = 0
                for user in data:
                    if user['coin'] > biggest:
                        biggest = user['coin']
                        biggest_id = user
                
                
            # leaderboard
        logging.info(f'Received data: {user_data}')
        # print('Received GET request')
        # print('Path:', self.path)
        # print('Headers:\n', self.headers)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response.encode())

def validation(username, password):
    data = read_from_json_file('database.json')
    print("Data from JSON file:", data)  # Debugging statement
    for user in data:
        if user['username'] == username or user['password'] == password:
            return True, user['id']
    return False, user['id']

# def validation(username,password):
#     data = read_from_json_file('database.json')
#     for i in data[0]:
#         if i['username'] == username and i['password'] == password:
#             return True
#     return False
    

def run_http_server():
    server_address = (server_ip, 8080)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print('HTTP server running on port 8080')
    httpd.serve_forever()

# Socket Server setup
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
        
        if data:
            print('Received data:', data.decode())
            logging.info(f'Received data: {data.decode()}')
        client_socket.sendall(b'Hello from Socket server!')
        client_socket.close()

# Run both servers concurrently
http_thread = threading.Thread(target=run_http_server)
socket_thread = threading.Thread(target=run_socket_server)

write_to_json_file('database.json', data)

print(data)
http_thread.start()
socket_thread.start()
http_thread.join()
socket_thread.join()
