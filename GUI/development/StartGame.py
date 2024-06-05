# Nama File : StartGame.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : Rabu, 22 Mei 2024 ; Jumat, 31 Mei 2024

import tkinter as tk
from tkinter import ttk
from Matchmaking import *
from display_active_user import *
import client1 as c

def show_start_game_page(root, show_main_page_func, show_login_page_func, user):
    for widget in root.winfo_children():
        widget.destroy()

    # Meminta dari server daftar pemain lain yang sudah stand-by di waiting room / sudah klik 'Start Game'
    data = eval(c.http_client([id_become_active, user]))  # dari string diubah ke array

    list_active_player = data
    # print(list_active_player) # DEBUG
    display_active_users(root, list_active_player)  # menampilkan list user aktif (GUI)

    # GUI
    root.title('Start Game')
    root.configure(bg='#f0f0f0')  # Background color

    title_label = ttk.Label(root, text="Start Game Page", font=("Helvetica", 18, "bold"), foreground="#333")
    title_label.pack(pady=20)

    button_style = {
        "font": ("Helvetica", 12, "bold"),
        "bg": "#4CAF50",
        "fg": "white",
        "activebackground": "#45a049",
        "activeforeground": "white",
        "relief": "raised",
        "bd": 3
    }

    # # Back button
    # back_button = tk.Button(root, text="Back to Main", command=lambda: show_main_page_func(root, show_login_page_func, user), **button_style)
    # back_button.pack(fill='x', expand=True, padx=20, pady=5)

    # Tambahkan tombol untuk random matchmaking
    random_matchmaking_button = tk.Button(root, text="Random Matchmaking", command=lambda: show_random_matchmaking_func(root, show_start_game_page, show_main_page_func, show_login_page_func, user), **button_style)
    random_matchmaking_button.pack(fill='x', expand=True, padx=20, pady=5)

    # Tambahkan tombol untuk targeted matchmaking
    targeted_matchmaking_button = tk.Button(root, text="Targeted Matchmaking", command=lambda: show_targeted_matchmaking_func(root, show_start_game_page, show_main_page_func, show_login_page_func, user), **button_style)
    targeted_matchmaking_button.pack(fill='x', expand=True, padx=20, pady=0)

    # Customize back button
    back_button = tk.Button(root, text="Back to Main", command=lambda: show_main_page_func(root, show_login_page_func, user),
                            bg="#ff6666", fg="white", font=("Helvetica", 10, "bold"))
    back_button.place(relx=0.95, rely=1, anchor="se")  # Place the button at the bottom-right corner


# # Test the function
# if __name__ == "__main__":
#     root = tk.Tk()
#     show_start_game_page(root, lambda x, y, z: None, lambda x: None, "test_user")
#     root.mainloop()

# END_OF_FILE[]
