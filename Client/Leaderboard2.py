# Nama File : Leaderboard.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : Rabu, 22 Mei 2024 ; Jumat, 31 Mei 2024

import tkinter as tk
from tkinter import ttk
import display_leaderboard2 as dl
import client2 as c
from constant import *

def show_leaderboard_page(root, show_main_page_func, show_login_page_func, user):
    for widget in root.winfo_children():
        widget.destroy()

    root.title('Leaderboard')

    title_label = ttk.Label(root, text="Leaderboard Page", font=("Helvetica", 18, "bold"), foreground="#333")
    title_label.pack(pady=10)

    data = eval(c.socket_client([id_leaderboard_request, user]))  # dari string diubah ke array
    print(data)
    dl.show_leaderboard(root, data)

    # Customize back button
    back_button = tk.Button(root, text="Back to Main", command=lambda: show_main_page_func(root, show_login_page_func, user),
                            bg="#ff6666", fg="white", font=("Helvetica", 10, "bold"))
    back_button.place(relx=0.95, rely=0.95, anchor="se")  # Place the button at the bottom-right corner

# END_OF_FILE[]
