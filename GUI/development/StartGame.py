# Nama File : StartGame.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : Rabu, 22 Mei 2024 ; Jumat, 31 Mei 2024

import tkinter as tk
from tkinter import ttk
# from Matchmaking2 import *
from Matchmaking import *
from display_active_user import *
import client1 as c

def show_start_game_page(root, show_main_page_func, show_login_page_func, user):
    for widget in root.winfo_children():
        widget.destroy()

    # Meminta dari server daftar pemain lain yang sudah stand-by di waiting room / sudah klik 'Start Game'
    data = eval(c.http_client([id_become_active,user])) # dari string diubah ke array

    list_active_player = data
    # for k in range(data):
    #     print(k,player[k],sep=". ")
    print(list_active_player) # DEBUG
    display_active_users(root, list_active_player) # menampilkan list user aktif (GUI)

    # GUI
    root.title('Start Game')
    title_label = ttk.Label(root, text="Start Game Page", font=("Helvetica", 18))
    title_label.pack(pady=20)

    back_button = ttk.Button(root, text="Back to Main", command=lambda: show_main_page_func(root, show_login_page_func, user))
    back_button.pack(fill='x', expand=True, padx=20, pady=5)

    # Tambahkan tombol untuk random matchmaking
    random_matchmaking_button = ttk.Button(root, text="Random Matchmaking", command=lambda: show_random_matchmaking_func(root, show_start_game_page, show_main_page_func, show_login_page_func,user))
    random_matchmaking_button.pack(fill='x', expand=True, padx=20, pady=5)

    # Tambahkan tombol untuk targeted matchmaking
    targeted_matchmaking_button = ttk.Button(root, text="Targeted Matchmaking", command=lambda: show_targeted_matchmaking_func(root, show_start_game_page, show_main_page_func, show_login_page_func,user))
    targeted_matchmaking_button.pack(fill='x', expand=True, padx=20, pady=5)

# END_OF_FILE[]