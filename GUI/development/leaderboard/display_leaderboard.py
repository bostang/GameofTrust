import tkinter as tk
from tkinter import ttk

def create_leaderboard(root, data):
    # Clear existing widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Extract data
    leaderboard_data = data[1]
    special_user = data[2]

    # Combine leaderboard data with special user
    all_users_data = leaderboard_data + [[special_user[0], special_user[2]]]

    # Sort the combined data based on coins in descending order
    sorted_users_data = sorted(all_users_data, key=lambda x: x[1] if len(x) > 1 else 0, reverse=True)

    # Create a frame for the leaderboard
    leaderboard_frame = ttk.Frame(root, padding="10")
    leaderboard_frame.pack(fill='both', expand=True)

    # Title
    title_label = ttk.Label(leaderboard_frame, text="Leaderboard", font=("Helvetica", 16))
    title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

    # Create Treeview
    columns = ("Rank", "Username", "Coins")
    leaderboard_table = ttk.Treeview(leaderboard_frame, columns=columns, show="headings", height=len(sorted_users_data))
    leaderboard_table.heading("Rank", text="Rank")
    leaderboard_table.heading("Username", text="Username")
    leaderboard_table.heading("Coins", text="Coins")
    leaderboard_table.column("Rank", width=50)
    leaderboard_table.column("Username", width=150)
    leaderboard_table.column("Coins", width=100)
    leaderboard_table.grid(row=1, column=0, columnspan=3)

    special_user_rank = next(rank for rank, (username, _) in enumerate(sorted_users_data, start=1) if username == special_user[0])

    # Add data to the Treeview with ranks, highlight special user if in top 10
    for rank, (username, coins) in enumerate(sorted_users_data, start=1):
        if rank <= 10:
            if username == special_user[0]:
                leaderboard_table.insert("", "end", values=(rank, username, coins), tags=('special_user',))
            else:
                leaderboard_table.insert("", "end", values=(rank, username, coins))

    # Highlight the special user row
    leaderboard_table.tag_configure('special_user', background='lightblue')

    # If special user is not in top 10, display separately with an empty row
    if special_user_rank > 10:
        leaderboard_table.insert("", "end", values=("", "", ""))
        # leaderboard_table.insert("", "end", values=(special_user_rank, special_user[0], special_user[2]), tags=('special_user',))
        leaderboard_table.insert("", "end", values=(special_user[1], special_user[0], special_user[2]), tags=('special_user',))

    # Special user display
    special_user_label = ttk.Label(leaderboard_frame, text=f"Special User: {special_user[0]} is ranked #{special_user_rank} with {special_user[2]} coins", font=("Helvetica", 12))
    special_user_label.grid(row=2, column=0, columnspan=3, pady=(10, 0))

def show_leaderboard_page(root):
    """Show the leaderboard page."""
    incoming_message_leaderboard = [
        2,
        [["bostang", 30], ["yansen", 25], ["kingkung",27],["kungkung",3],["kangkung",4],["kingking",9],["kwingkung",18],["kongking",72],["kwangkweng",70],["kinglung",60]],
        ["kunga", 17, 31]
    ]
    create_leaderboard(root, incoming_message_leaderboard)
    root.title('Leaderboard')
    root.geometry("400x500")  # Adjusted window size
    root.resizable(False, False)

if __name__ == "__main__":
    # root window
    root = tk.Tk()
    show_leaderboard_page(root)
    root.mainloop()
