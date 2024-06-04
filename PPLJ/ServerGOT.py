from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse
import threading
import socket
import logging
import ast
import json
from datetime import datetime
server_ip = "10.8.103.141"

matchmaking = [[0,0]]

timeout = 60

logging.basicConfig(
    filename='server.log',        # Log file name
    level=logging.DEBUG,          # Log level
    format='%(asctime)s %(levelname)s %(message)s'  # Log format
)

data = [
    {'id': 1, 'username': 'yansen','password':'phoenix' , 'coin': 30},
    {'id': 2, 'username': 'bostang','password':'tes' , 'coin': 20},
    {'id': 3, 'username': 'kunga','password':'tes' , 'coin': 10},
    {'id': 4, 'username': 'lord','password':'tes' , 'coin': 9999},
    {'id': 5, 'username': 'newbie','password':'tes' , 'coin': 0},
    {'id': 6, 'username': 'bostang','password':'tes' , 'coin': 5},
    {'id': 7, 'username': 'bostang','password':'tes' , 'coin': 9},
    
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
        # user_id = validation(username, password
        if msg_id == 1: #login request
            username = user_data_list[1]
            password = user_data_list[2]
            is_valid, user_id = validation(username, password, msg_id)
            # username = user_data_list[1]
            # password = user_data_list[2]
            if is_valid:
                print("Authentication successful")
                response = f'hello user {user_id}: {username}'
            else:
                response = f'hello, username: {username} and password: {password} already been used'
                print("Authentication failed")
            
        elif msg_id == 12: #sign in request
            username = user_data_list[1]
            password = user_data_list[2]
            is_valid, user_id = validation(username, password, msg_id)
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
            sorted_data = sorted(data, key=lambda x: x["coin"], reverse=True)[:10]
            leaderboard = [[item['username'], item['coin']] for item in sorted_data]
            i = 0
            username_coin = 0
            for user in sorted_data:
                i += 1
                if user["username"] == username:
                    username_coin = user["coin"]
                    ranking = i
            player_leaderboard = [username,username_coin,ranking]
            response = f'21,{leaderboard},{player_leaderboard}'
        
        elif msg_id == 3: # room join
            username = user_data_list[1]
            id = get_id(username)
            matchmaking_id = user_data_list[2]
            print(matchmaking_id)

            if (matchmaking_id == 0):
                if (matchmaking[0][0] != 0):
                    # Make room
                    # Send request for client input
                    response = f'Found other player'
                    

                else:
                    match_found = False
                    start_time = datetime.now()
                    while (((datetime.now()-start_time).seconds <= timeout) or (match_found)):
                        if matchmaking[0][1] != 0:
                            match_found = True
                            break

                    if (not match_found):
                        # Return timeout to client
                        response = f'Timeout, other player not found'

                    else:
                        # Return found client
                        # Send request for client input
                        response = f'Found other player'

                    matchmaking[0] = [0, 0]


            else:
                match_found = False

                for matchmaking_room in matchmaking:
                    if (matchmaking_room[0] == id):
                        match_found = True
                        break

                if (match_found):
                    # Make room
                    # Send request for client input
                    response = f'Found other player'

                else:
                    matchmaking.append([id, 0])
                    
                    match_found = False
                    start_time = datetime.now()
                    while (((datetime.now()-start_time).seconds <= timeout) or (match_found)):
                        for matchmaking_room in matchmaking:
                            if (matchmaking_room[0] == id):
                                if matchmaking_room[1] != 0:
                                    match_found = True
                                break

                    if (not match_found):
                        # Return timeout to client
                        response = f'Timeout, other player not found'
                    else:
                        # Return found client
                        # Send request for client input
                        response = f'Found other player'
                    
                    current_index = next((index for (index, d) in enumerate(matchmaking) if d[0] == id))
                    del matchmaking[current_index]
                
            # leaderboard
        logging.info(f'Received data: {user_data}')
        # print('Received GET request')
        # print('Path:', self.path)
        # print('Headers:\n', self.headers)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response.encode())

def get_id(username):
    data = read_from_json_file('database.json')
    print("Data from JSON file:", data)  # Debugging statement
    for user in data:
        if user['username'] == username:
            return user['id']
            
    return 0

def validation(username, password,id):
    data = read_from_json_file('database.json')
    print("Data from JSON file:", data)  # Debugging statement
    for user in data:
        if user['username'] == username and user['password'] == password and id == 1:
            return True, user['id']
        elif user['username'] == username and id == 2:
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
