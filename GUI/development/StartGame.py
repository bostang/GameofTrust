# Nama File : StartGame.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : Rabu, 22 Mei 2024 ; Jumat, 31 Mei 2024

import tkinter as tk
from tkinter import ttk

# def show_start_game_page(root, show_main_page_func):
def show_start_game_page(root, show_main_page_func, show_login_page_func):
    for widget in root.winfo_children():
        widget.destroy()

    root.title('Start Game')
    title_label = ttk.Label(root, text="Start Game Page", font=("Helvetica", 18))
    title_label.pack(pady=20)

    # back_button = ttk.Button(root, text="Back to Main", command=lambda: show_main_page_func(root))
    back_button = ttk.Button(root, text="Back to Main", command=lambda: show_main_page_func(root, show_login_page_func))
    back_button.pack(fill='x', expand=True, padx=20, pady=5)

# END_OF_FILE[]