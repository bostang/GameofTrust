# Nama File : Login.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : 
    # Minggu, 12 Mei 2024
    # Rabu, 22 Mei 2024
    # Jumat, 31 Mei 2024

# import library
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from MainPage import show_main_page  # Import fungsi untuk menampilkan halaman utama


def create_login_page(root):
    """Create the login page."""
    # Clear existing widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    # store username dan password
    username = tk.StringVar()
    password = tk.StringVar()

    # Load user data dari file
    def load_user_data(file_path):
        users = {}
        with open(file_path, 'r') as file:
            for line in file:
                id,user, pwd, coins = line.strip().split(',')
                users[user] = pwd
        return users

    # Load user data
    user_data = load_user_data('database.txt')

    def login_clicked():
        """ callback ketika tombol login diklik
        """
        user = username.get()
        pwd = password.get()
        if user in user_data and user_data[user] == pwd:
            showinfo(
                title='Information',
                message=f'Welcome {user}!'
            )
            # After successful login, show the main page
            show_main_page(root, show_login_page)  # Panggil fungsi untuk menampilkan halaman utama
        else:
            showerror(
                title='Error',
                message='Invalid username or password'
            )

    # Sign in frame
    signin = ttk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=True)

    # username
    username_label = ttk.Label(signin, text="Username:")
    username_label.pack(fill='x', expand=True)

    username_entry = ttk.Entry(signin, textvariable=username)
    username_entry.pack(fill='x', expand=True)
    username_entry.focus()

    # password
    password_label = ttk.Label(signin, text="Password:")
    password_label.pack(fill='x', expand=True)

    password_entry = ttk.Entry(signin, textvariable=password, show="*")
    password_entry.pack(fill='x', expand=True)

    # login button
    login_button = ttk.Button(signin, text="Login", command=login_clicked)
    login_button.pack(fill='x', expand=True, pady=10)

def show_login_page(root):
    """Show the login page."""
    create_login_page(root)
    root.title('Sign In')
    root.geometry("300x150")
    root.resizable(False, False)
    root.iconbitmap('./img/logo_2.ico')  # Menambahkan logo

if __name__ == "__main__":
    # root window
    root = tk.Tk()
    show_login_page(root)
    root.mainloop()  # Ensure the main event loop starts after showing the login page


# Referensi
# 1. https://www.pythontutorial.net/tkinter/tkinter-entry/

# END_OF_FILE[]
