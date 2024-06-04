# Nama File : client1.py
# Programmer : 
    #   Yansen Dwi Putra (13220056)
    #   Bostang Palaguna (13220055)
# Tanggal : 
    # Minggu, 2 Juni 2024
    # Selasa, 4 Juni 2024

# Import Library
import requests
import json
from constant import *

def http_client(data_list):
    # Fungsi ini mengirimkan data_list ke server HTTP dan mengembalikan respons dari server.
    # Format pemanggilan: http_client([msgId,Username])
    
    # IP target server
    target_ip = "192.168.116.240"
    
    # Cetak data_list untuk debugging
    print("data list:",data_list,sep=' ')
    
    # Mengonversi data_list menjadi JSON
    json_data = json.dumps(data_list)
    
    # Membentuk URL dengan data JSON
    url = f'http://{target_ip}:8080?data={json_data}'
    
    # Mengirimkan permintaan GET ke server
    response = requests.get(url)
    
    # Cetak respons dari server untuk debugging
    print('HTTP Server Response:', response.text)
    
    # Mengembalikan respons dari server dalam bentuk teks
    return response.text
