# Nama File : MainPage.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : Rabu, 22 Mei 2024; Jumat, 31 Mei 2024

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Profile import show_profile_page
from StartGame import show_start_game_page
from Leaderboard import show_leaderboard_page
from constant import *
import client1 as c

def show_main_page(root, show_login_page_func, user):
    
    # Menandakan dia sebagai in-active (catatan : aktif ketika klik start game)
    data = eval(c.http_client([id_become_inactive, user])) # dari string diubah ke array

    # GUI
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("400x400")
    root.title('Main Page')
    root.iconbitmap('./img/logo_2.ico')  # Menambahkan logo

    title_label = ttk.Label(root, text="Game of Trust", font=("Helvetica", 24, "bold"), foreground="#333")
    title_label.pack(pady=20)

    # Load an application image
    logo = tk.PhotoImage(file='./img/logo_2.png')

    # Display image in a label
    logo_label = tk.Label(root, image=logo)
    logo_label.image = logo  # Keep a reference to the image to avoid garbage collection
    logo_label.pack(pady=10)

    # title_label = ttk.Label(root, text="Main Page", font=("Helvetica", 24, "bold"), foreground="#333")
    title_label.pack(pady=10)
    # Logout button
    logout_button = tk.Button(root, text="Logout", command=lambda: show_login_page_func(root), bg="#ff6666", fg="white", font=("Helvetica", 10, "bold"))
    logout_button.place(relx=1, rely=0.05, anchor="ne")

    # Start Game button
    start_game_button = tk.Button(root, text="Start Game", command=lambda: show_start_game_page(root, show_main_page, show_login_page_func, user), 
                                  bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
    start_game_button.pack(fill='x', expand=True, padx=20, pady=10)

    # Leaderboard button
    leaderboard_button = tk.Button(root, text="Leaderboard", command=lambda: show_leaderboard_page(root, show_main_page, show_login_page_func, user), 
                                   bg="#008CBA", fg="white", font=("Helvetica", 12, "bold"))
    leaderboard_button.pack(fill='x', expand=True, padx=20, pady=10)

# END_OF_FILE[]
