import tkinter as tk
from game_logic import Player, COOPERATE, CHEAT, trust_game
import uuid

# Create players
player1 = Player("Player 1", uuid.uuid4())
player2 = Player("Player 2", uuid.uuid4())

def create_player_window(player, other_player, result_label):
    def on_decision(decision):
        player.decision = decision
        if player1.decision is not None and player2.decision is not None:
            result = trust_game(player1, player2)
            result_label.config(text=result)
            # Reset decisions for next round
            player1.decision, player2.decision = None, None

    window = tk.Toplevel()
    window.title(f"{player.name}'s Decision")

    label = tk.Label(window, text=f"{player.name}, choose your action:")
    label.pack(pady=10)

    cooperate_button = tk.Button(window, text="Cooperate", command=lambda: on_decision(COOPERATE))
    cooperate_button.pack(side=tk.LEFT, padx=5, pady=5)

    cheat_button = tk.Button(window, text="Cheat", command=lambda: on_decision(CHEAT))
    cheat_button.pack(side=tk.LEFT, padx=5, pady=5)

def create_main_window():
    root = tk.Tk()
    root.title("Trust Game")

    instruction_label = tk.Label(root, text="Players, make your decisions in your respective windows.")
    instruction_label.pack(pady=10)

    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    # Create player windows
    create_player_window(player1, player2, result_label)
    create_player_window(player2, player1, result_label)

    root.mainloop()

# Example usage
if __name__ == "__main__":
    create_main_window()
