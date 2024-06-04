# Nama File : main.py
# Programmer : Bostang Palaguna (13220055)
# Tanggal : Minggu, 12 Mei 2024

# import library
import tkinter as tk
from tkinter import ttk # themed tkinter widget
from tkinter.messagebox import showinfo

root = tk.Tk() # create the application window
title = "Game of Trust Demo"

root.title(title) # Changing the window title

# Changing window size and location
window_width = 1366
window_height = 768

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False) # prevent the window from resizing

# place a label on the root window
message = tk.Label(root, text="Welcome to the Game of Trust!") # creates a Label widget placed on the root window:
message.pack() # make the widget visible

root.iconbitmap('./img/logo_2.ico') # mengatur logo

# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# Start button handler
def start_clicked():
    showinfo(
        title='Information',
        message='Download button clicked!'
    )


download_icon = tk.PhotoImage(file='./img/start.png')
resized_download_icon = download_icon.subsample(2)  # Change the value to adjust the size (e.g., subsample(2) halves the size)

download_button = ttk.Button(
    root,
    image=resized_download_icon,
    text='',
    compound=tk.LEFT,
    command=start_clicked
)

download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# Agreement Button
agreement = tk.StringVar()


def agreement_changed():
    tk.messagebox.showinfo(title='Result',
                        message=agreement.get())


ttk.Checkbutton(root,
                text='I agree',
                command=agreement_changed,
                variable=agreement,
                onvalue='agree',
                offvalue='disagree').pack()

# Radio button
def show_selected_size():
    showinfo(
        title='Result',
        message=selected_size.get()
    )


selected_size = tk.StringVar()
sizes = (('Small', 'S'),
         ('Medium', 'M'),
         ('Large', 'L'),
         ('Extra Large', 'XL'),
         ('Extra Extra Large', 'XXL'))

# label
label = ttk.Label(text="What's your t-shirt size?")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected_size
    )
    r.pack(fill='x', padx=5, pady=5)

# button
button = ttk.Button(
    root,
    text="Get Selected Size",
    command=show_selected_size)

button.pack(fill='x', padx=5, pady=5)


root.mainloop() # method of the main window object 
                # ensures the main window remains visible on the screen)
                # ensures the main window continues to display and run until you close it


# Referensi
    # 1. https://www.pythontutorial.net/tkinter/