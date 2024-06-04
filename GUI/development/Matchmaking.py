# Nama File : Matchmaking.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : Selasa, 4 Juni 2024

import tkinter as tk
from tkinter import ttk

def show_random_matchmaking_func(root, show_start_game_page_func, show_main_page, show_login_page_func,user):
    for widget in root.winfo_children():
        widget.destroy()

    root.title('Start Game')
    title_label = ttk.Label(root, text="Start Game Page", font=("Helvetica", 18))
    title_label.pack(pady=20)

    back_button = ttk.Button(root, text="Back to Matchmaking", command=lambda: show_start_game_page_func(root, show_main_page, show_login_page_func,user))
    back_button.pack(fill='x', expand=True, padx=20, pady=5)

def show_targeted_matchmaking_func(root, show_start_game_page_func, show_main_page, show_login_page_func,user):
    for widget in root.winfo_children():
        widget.destroy()

    root.title('Start Game')
    title_label = ttk.Label(root, text="Start Game Page", font=("Helvetica", 18))
    title_label.pack(pady=20)

    # back_button = ttk.Button(root, text="Back to Main", command=lambda: show_main_page_func(root))
    back_button = ttk.Button(root, text="Back to Matchmaking", command=lambda: show_start_game_page_func(root, show_main_page, show_login_page_func,user))
    back_button.pack(fill='x', expand=True, padx=20, pady=5)


# END_OF_FILE[]