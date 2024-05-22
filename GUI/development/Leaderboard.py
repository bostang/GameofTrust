# Nama File : Leaderboard.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : Rabu, 22 Mei 2024

import tkinter as tk
from tkinter import ttk

def show_leaderboard_page():
    root = tk.Tk()
    root.geometry("400x300")
    root.title('Leaderboard')
    root.iconbitmap('./img/logo_2.png')  # Menambahkan logo

    label = ttk.Label(root, text="Leaderboard Page", font=("Helvetica", 18))
    label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    show_leaderboard_page()
