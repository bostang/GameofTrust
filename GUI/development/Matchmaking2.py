# Nama File : Matchmaking.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : Selasa, 4 Juni 2024

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from constant import *
import client1 as c

def show_random_matchmaking_func(root, show_start_game_page_func, show_main_page_func, show_login_page_func,user):
    # ini adalah callback function ketika button 'start random matchmaking' ditekan

    # mengirim request ke server
    data = eval(c.http_client([id_room_join,user,""])) # dari string diubah ke array
    print("sukses bos!")
    # data = true -> matchmaking berhasil, memulai permainan
    # data = false -> timeout, balik ke start game
    
    # ketika timeout, balik ke start game lagi, kasih message
    if (not data): # timeout
        showinfo(
        title='Timeout matchmaking',
        message=f'Anda terkena timeout!'
        )
        # kembali ke halaman sebelumnya
        # show_start_game_page_func(root, show_main_page, show_login_page_func,user);
        show_main_page_func(root, show_login_page_func,user)
    else: # lanjut main
        showinfo(
        title='Sukses matchmaking',
        message=f'Anda terhubung dengan lawan!'
        )

    # bagian GUI
    for widget in root.winfo_children():
        widget.destroy()

    root.title('Random matchmaking')
    title_label = ttk.Label(root, text="Randopm matchmaking", font=("Helvetica", 18))
    title_label.pack(pady=20)

    # button untuk cooperate / cheat
    def on_cooperate():
        data = eval(c.http_client([id_match_start,user,COOPERATE]))
        showinfo(
        title='Cooperate chosen',
        message=f'Anda memilih kooperasi!\npoin anda:{data[0]}\npoin lawan:{data[1]}'
        )
        # kembali lagi ke main menu
        # show_start_game_page_func(root, show_main_page, show_login_page_func,user);
        show_main_page_func(root, show_login_page_func,user)

    def on_cheat():
        data = eval(c.http_client([id_match_start,user,CHEAT]))
        showinfo(
        title='Cheat chosen',
        message=f'Anda memilih cheating!\npoin anda:{data[0]}\npoin lawan:{data[1]}'
        )
        # kembali lagi ke main menu
        # show_start_game_page_func(root, show_main_page, show_login_page_func,user);
        show_main_page_func(root, show_login_page_func,user)

    # Warna latar belakang dan teks untuk tombol 'Cooperate'
    cooperate_button = tk.Button(root, text="Cooperate", command=on_cooperate, bg="#4CAF50", fg="white")
    cooperate_button.config(font=("Arial", 12))
    cooperate_button.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.BOTH)

    # Warna latar belakang dan teks untuk tombol 'Cheat'
    cheat_button = tk.Button(root, text="Cheat", command=on_cheat, bg="#f44336", fg="white")
    cheat_button.config(font=("Arial", 12))
    cheat_button.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.BOTH)


    # back button
    back_button = ttk.Button(root, text="Back to Matchmaking", command=lambda: show_start_game_page_func(root, show_main_page, show_login_page_func,user))
    back_button.pack(fill='x', expand=True, padx=20, pady=5)

def show_targeted_matchmaking_func(root, show_start_game_page_func, show_main_page_func, show_login_page_func,user):
    # ini adalah callback function ketika button 'start targeted matchmaking' ditekan

    # mengirim request ke server
    
    # bagian GUI
    for widget in root.winfo_children():
        widget.destroy()

    root.title('Targeted matchmaking')
    title_label = ttk.Label(root, text="Targeted Matchmaking", font=("Helvetica", 18))
    title_label.pack(pady=20)

    # mencari id lawan
    enemy_username = tk.StringVar()
    
    def find_enemy_clicked():
        # menampilkan informasi lawan yang di-klik
        showinfo(
            title='Enemy Info',
            message=f'Enemy looked for: {enemy_username.get()}!'
        ) 

        # melakukan matchmaking den
    # find enemy entry
    find_enemy_entry = ttk.Entry(root, textvariable=enemy_username)
    find_enemy_entry.pack(fill='x', expand=True)

    # find enemy button
    find_enemy_button = ttk.Button(root, text="Find", command=find_enemy_clicked)
    find_enemy_button.pack(fill='x', expand=True, pady=10)

    
    # back_button = ttk.Button(root, text="Back to Main", command=lambda: show_main_page_func(root))
    back_button = ttk.Button(root, text="Back to Matchmaking", command=lambda: show_start_game_page_func(root, show_main_page, show_login_page_func,user))
    back_button.pack(fill='x', expand=True, padx=20, pady=5)


# END_OF_FILE[]