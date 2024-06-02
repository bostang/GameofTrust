import requests
import json

def http_client():
    target_ip = "10.8.103.141"
    user_input = input("Enter data to send to the HTTP server: ")
    data_list =user_input.split(',')
    print(data_list)
    json_data = json.dumps(data_list)
    url = f'http://{target_ip}:8080?data={json_data}'
    response = requests.get(url)
    return response
    print('HTTP Server Response:', resaponse.text)

if __name__ == '__main__':
    while(1):
        tes = http_client()
