# Nama File : MainPage.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : Rabu, 22 Mei 2024

import tkinter as tk
from tkinter import ttk
from trust_game_gui import create_player_window
from game_logic import Player, COOPERATE, CHEAT, trust_game
import uuid

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

    start_button = ttk.Button(root, text="Start the Game", command=lambda: start_game(root))
    start_button.pack(fill='x', expand=True, padx=20, pady=5)

    back_button = ttk.Button(root, text="Back to Main", command=lambda: show_main_page(root))
    back_button.pack(fill='x', expand=True, padx=20, pady=5)

def start_game(root):
    root.withdraw()  # Hide the main window

    def on_game_end():
        root.deiconify()  # Show the main window again
        show_main_page(root)

    # Create players
    player1 = Player("Player 1", uuid.uuid4())
    player2 = Player("Player 2", uuid.uuid4())

    result_label = tk.Label(root, text="")
    create_player_window(player1, player2, result_label, on_game_end)
    create_player_window(player2, player1, result_label, on_game_end)

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

if __name__ == "__main__":
    root = tk.Tk()
    show_main_page(root)
    root.mainloop()
