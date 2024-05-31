# Nama File : MainPage.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : Rabu, 22 Mei 2024

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def show_main_page(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("400x300")
    root.title('Main Page')
    root.iconbitmap('./img/logo_2.ico')  # Menambahkan logo

    title_label = ttk.Label(root, text="Main Page", font=("Helvetica", 24))
    title_label.pack(pady=20)

    start_game_button = ttk.Button(root, text="Start Game", command=lambda: show_start_game_page(root))
    start_game_button.pack(fill='x', expand=True, padx=20, pady=5)

    leaderboard_button = ttk.Button(root, text="Leaderboard", command=lambda: show_leaderboard_page(root))
    leaderboard_button.pack(fill='x', expand=True, padx=20, pady=5)

    profile_button = ttk.Button(root, text="Profile", command=lambda: show_profile_page(root))
    profile_button.pack(fill='x', expand=True, padx=20, pady=5)

def show_start_game_page(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title('Start Game')
    title_label = ttk.Label(root, text="Start Game Page", font=("Helvetica", 18))
    title_label.pack(pady=20)

    back_button = ttk.Button(root, text="Back to Main", command=lambda: show_main_page(root))
    back_button.pack(fill='x', expand=True, padx=20, pady=5)

def show_leaderboard_page(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title('Leaderboard')
    title_label = ttk.Label(root, text="Leaderboard Page", font=("Helvetica", 18))
    title_label.pack(pady=20)

    back_button = ttk.Button(root, text="Back to Main", command=lambda: show_main_page(root))
    back_button.pack(fill='x', expand=True, padx=20, pady=5)

def show_profile_page(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title('Profile')
    title_label = ttk.Label(root, text="Profile Page", font=("Helvetica", 18))
    title_label.pack(pady=20)

    back_button = ttk.Button(root, text="Back to Main", command=lambda: show_main_page(root))
    back_button.pack(fill='x', expand=True, padx=20, pady=5)