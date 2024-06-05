import tkinter as tk

def display_active_users(root, users):
    for user in users:
        frame = tk.Frame(root)
        frame.pack(anchor='w', pady=2)
        
        # Create a green circle
        canvas = tk.Canvas(frame, width=20, height=20, bg="white", highlightthickness=0)
        canvas.create_oval(2, 2, 18, 18, fill="green")
        canvas.pack(side='left')
        
        # Create a label for the user name
        label = tk.Label(frame, text=user)
        label.pack(side='left', padx=5)

# def display_active_users(users):
#     for user in users:
#         frame = tk.Frame(root)
#         frame.pack(anchor='w', pady=2)
        
#         # Create a green circle
#         canvas = tk.Canvas(frame, width=20, height=20, bg="white", highlightthickness=0)
#         canvas.create_oval(2, 2, 18, 18, fill="green")
#         canvas.pack(side='left')
        
#         # Create a label for the user name
#         label = tk.Label(frame, text=user)
#         label.pack(side='left', padx=5)

#         # Create the main window
#         root = tk.Tk()
#         root.title("Active Players")

# # List of active users
# active_users = ["Alice", "Bob", "Charlie", "David"]

# # Create the main window
# root = tk.Tk()
# root.title("Active Players")

# # Display active users with green circles
# display_active_users(active_users)

# # Run the Tkinter event loop
# root.mainloop()
