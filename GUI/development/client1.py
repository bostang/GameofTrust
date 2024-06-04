# Konstanta
id_login = 1
id_register = 12

import requests
import json

def http_client(data_list):
    # format pemanggilan : http_client([msgId,Username])
    target_ip = "10.8.105.197"
    # target_ip = "192.168.116.240"
    # user_input = input("Enter data to send to the HTTP server: ")
    # data_list =user_input.split(',')
    print("data list:",data_list,sep=' ')
    
    json_data = json.dumps(data_list)
    url = f'http://{target_ip}:8080?data={json_data}'
    response = requests.get(url)
    print('HTTP Server Response:', response.text)
    return response.text
    

# if __name__ == '__main__':
#     while(1):
#         tes = http_client()
