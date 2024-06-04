import socket
import json
from constant import *

def socket_client(data_list):
    target_ip = "10.8.102.118"
    # user_input = input("Enter data to send to the Socket server: ")
    # data_list = user_input.split(',')
    user_input = ','.join(map(str, data_list))
    json_data = json.dumps(data_list)
    
    server_address = (target_ip, 65432)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server_address)
        s.sendall(user_input.encode())
        data = s.recv(1024)
    
    print('Socket Server Response:', data.decode())
    return data

if __name__ == '__main__':
    while(1):
        socket_client()