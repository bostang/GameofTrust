# Nama File : Login.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : 
    # Minggu, 12 Mei 2024
    # Rabu, 22 Mei 2024
    # Jumat, 31 Mei 2024
    # Minggu, 2 Juni 2024
    # Rabu, 4 Juni 2024

# import library
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from MainPage2 import show_main_page  # Import fungsi untuk menampilkan halaman utama
from client2 import *

def create_login_page(root):
    """Create the login page."""
    # Clear existing widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    # store username dan password
    username = tk.StringVar()
    password = tk.StringVar()

    def login_clicked():
        """ callback ketika tombol login diklik
        """
        user = username.get()
        pwd = password.get()
        login_valid = eval(socket_client([id_login,user,pwd]))
        if (login_valid):
            showinfo(
                title='Information',
                message=f'Welcome {user}!'
            )
            # After successful login, show the main page
            show_main_page(root, show_login_page,user)  # Panggil fungsi untuk menampilkan halaman utama
        else:
            showerror(
                title='Error',
                message='Invalid username or password'
            )

    def register_clicked():
        """ callback ketika tombol register diklik
        """
        user = username.get()
        pwd = password.get()

        user_exist = eval(socket_client([id_register,user,pwd]));
        print(f"user exist:{user_exist}") # DEBUG
        if (user_exist):
            showerror(
                title='Error',
                message='Username already exists'
            )
        else:
            with open('users.txt', 'a') as file:
                file.write(f'{user},{pwd}\n')
            showinfo(
                title='Information',
                message='Registration successful!'
            )
            # Optionally clear the entry fields after registration
            username.set('')
            password.set('')

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

    # register button
    register_button = ttk.Button(signin, text="Register", command=register_clicked)
    register_button.pack(fill='x', expand=True, pady=10)

def show_login_page(root):
    """Show the login page."""
    create_login_page(root)
    root.title('Sign In')
    root.geometry("300x200")
    root.resizable(False, False)
    root.iconbitmap('./img/logo_2.ico')  # Menambahkan logo

if __name__ == "__main__":
    # root window
    root = tk.Tk()
    show_login_page(root)
    root.mainloop()  # Ensure the main event loop starts after showing the login page


# Referensi
# 1. sockets://www.pythontutorial.net/tkinter/tkinter-entry/

# END_OF_FILE[]
