import tkinter as tk
from game_logic import Player, COOPERATE, CHEAT, trust_game
import uuid

def create_gui():
    def on_decision(player, decision):
        player.decision = decision
        if player1.decision is not None and player2.decision is not None:
            result = trust_game(player1, player2)
            result_label.config(text=result)
            # Reset decisions for next round
            player1.decision, player2.decision = None, None

    root = tk.Tk()
    root.title("Trust Game")

    frame1 = tk.Frame(root)
    frame1.pack(pady=10)

    player1_label = tk.Label(frame1, text="Player 1")
    player1_label.pack(side=tk.LEFT, padx=5)

    player1_cooperate_button = tk.Button(frame1, text="Cooperate", command=lambda: on_decision(player1, COOPERATE))
    player1_cooperate_button.pack(side=tk.LEFT, padx=5)

    player1_cheat_button = tk.Button(frame1, text="Cheat", command=lambda: on_decision(player1, CHEAT))
    player1_cheat_button.pack(side=tk.LEFT, padx=5)

    frame2 = tk.Frame(root)
    frame2.pack(pady=10)

    player2_label = tk.Label(frame2, text="Player 2")
    player2_label.pack(side=tk.LEFT, padx=5)

    player2_cooperate_button = tk.Button(frame2, text="Cooperate", command=lambda: on_decision(player2, COOPERATE))
    player2_cooperate_button.pack(side=tk.LEFT, padx=5)

    player2_cheat_button = tk.Button(frame2, text="Cheat", command=lambda: on_decision(player2, CHEAT))
    player2_cheat_button.pack(side=tk.LEFT, padx=5)

    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()

# Example usage
if __name__ == "__main__":
    # Create players with their names
    player1 = Player("Player 1", uuid.uuid4())
    player2 = Player("Player 2", uuid.uuid4())

    # Run the GUI
    create_gui()