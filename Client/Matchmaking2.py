# Nama File : Matchmaking.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : Selasa, 4 Juni 2024

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from constant import *
import client2 as c

def show_random_matchmaking_func(root, show_start_game_page_func, show_main_page_func, show_login_page_func,user):
    # ini adalah callback function ketika button 'start random matchmaking' ditekan

    # mengirim request ke server
    data = eval(c.socket_client([id_room_join,user,""])) # dari string diubah ke array
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
        title_label = ttk.Label(root, text="Random matchmaking", font=("Helvetica", 18))
        title_label.pack(pady=20)

        # button untuk cooperate / cheat
        def on_cooperate():
            data = eval(c.socket_client([id_match_start,user,COOPERATE]))
            showinfo(
            title='Cooperate chosen',
            message=f'Anda memilih kooperasi!\npoin anda:{data[0]}\npoin lawan:{data[1]}'
            )
            # kembali lagi ke main menu
            show_main_page_func(root, show_login_page_func,user)

        def on_cheat():
            data = eval(c.socket_client([id_match_start,user,CHEAT]))
            showinfo(
            title='Cheat chosen',
            message=f'Anda memilih cheating!\npoin anda:{data[0]}\npoin lawan:{data[1]}'
            )
            # kembali lagi ke main menu
            show_main_page_func(root, show_login_page_func,user)

        # Warna latar belakang dan teks untuk tombol 'Cooperate'
        cooperate_button = tk.Button(root, text="Cooperate", command=on_cooperate, bg="#4CAF50", fg="white")
        cooperate_button.config(font=("Arial", 12))
        cooperate_button.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.BOTH)

        # Warna latar belakang dan teks untuk tombol 'Cheat'
        cheat_button = tk.Button(root, text="Cheat", command=on_cheat, bg="#f44336", fg="white")
        cheat_button.config(font=("Arial", 12))
        cheat_button.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.BOTH)
       
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
    opponent_username = tk.StringVar()
    
    def find_opponent_clicked():
        # menampilkan informasi lawan yang di-klik
        showinfo(
            title='opponent Info',
            message=f'opponent looked for: {opponent_username.get()}!'
        ) 
        # melakukan matchmaking dengan user lawan yang telah dicari
        data = c.socket_client([id_room_join,user,opponent_username.get()]) # dari string diubah ke array

        if (data == "__NOT_VALID__"): # username tidak valid
            showerror(
                title='Opponent not Valid Error',
                message='Opponent not found!'
            )

        # print()
        elif (not eval(data)): # ketika timeout, server return string : False
            showinfo(
            title='Timeout matchmaking',
            message=f'Anda terkena timeout!'
            )
            # kembali ke halaman sebelumnya
            show_main_page_func(root, show_login_page_func,user)
        else:
            showinfo(
            title='Success finding opponent!',
            message=f'Lawan berhasil ditemukan'
            ) 
                # membersihkan layar
            for widget in root.winfo_children():
                widget.destroy()
            # melakukan matchmaking dengan lawan yang dicari username-nya
                # button untuk cooperate / cheat
            def on_cooperate():
                data = eval(c.socket_client([id_match_start,user,COOPERATE]))
                showinfo(
                title='Cooperate chosen',
                message=f'Anda memilih kooperasi!\npoin anda:{data[0]}\npoin lawan:{data[1]}'
                )
                # kembali lagi ke main menu
                show_main_page_func(root, show_login_page_func,user)

            def on_cheat():
                data = eval(c.socket_client([id_match_start,user,CHEAT]))
                showinfo(
                title='Cheat chosen',
                message=f'Anda memilih cheating!\npoin anda:{data[0]}\npoin lawan:{data[1]}'
                )
                # kembali lagi ke main menu
                # membersihkan layar
                for widget in root.winfo_children():
                    widget.destroy()

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

    # find opponent entry
    find_opponent_entry_title = tk.Label(text="Enter Opponent name to look for:")
    find_opponent_entry_title.pack()
    find_opponent_entry = ttk.Entry(root, width=30, textvariable=opponent_username)
    find_opponent_entry.pack()

    # find opponent button
    find_opponent_button = ttk.Button(root, text="Find", command=find_opponent_clicked)
    find_opponent_button.pack(fill='x', expand=True, pady=10)

    # back_button = ttk.Button(root, text="Back to Main", command=lambda: show_main_page_func(root))
    back_button = ttk.Button(root, text="Back to Matchmaking", command=lambda: show_start_game_page_func(root, show_main_page_func, show_login_page_func,user))
    back_button.pack(fill='x', expand=True, padx=20, pady=5)


# END_OF_FILE[]