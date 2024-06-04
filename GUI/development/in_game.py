import tkinter as tk

def on_cooperate():
    root.destroy()
    return_value(1)

def on_cheat():
    root.destroy()
    return_value(2)

def return_value(value):
    print("Return value:", value)

# Membuat jendela utama
root = tk.Tk()
root.title("Game Choices")
root.geometry("300x150")

# Warna latar belakang dan teks untuk tombol 'Cooperate'
cooperate_button = tk.Button(root, text="Cooperate", command=on_cooperate, bg="#4CAF50", fg="white")
cooperate_button.config(font=("Arial", 12))
cooperate_button.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.BOTH)

# Warna latar belakang dan teks untuk tombol 'Cheat'
cheat_button = tk.Button(root, text="Cheat", command=on_cheat, bg="#f44336", fg="white")
cheat_button.config(font=("Arial", 12))
cheat_button.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.BOTH)

# Menjalankan aplikasi GUI
root.mainloop()
