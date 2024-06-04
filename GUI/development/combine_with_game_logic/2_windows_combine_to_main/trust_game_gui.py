import tkinter as tk
from game_logic import Player, COOPERATE, CHEAT, trust_game
import uuid

def create_player_window(player, other_player, result_label, on_game_end):
    def on_decision(decision):
        player.decision = decision
        if player1.decision is not None and player2.decision is not None:
            result = trust_game(player1, player2)
            result_label.config(text=result)
            # Reset decisions for next round
            player1.decision, player2.decision = None, None
            # Close both player windows
            player1_window.destroy()
            player2_window.destroy()
            # Call the callback function to go back to the main page
            on_game_end()

    player1_window = tk.Toplevel()
    player1_window.title(f"{player.name}'s Decision")

    label = tk.Label(player1_window, text=f"{player.name}, choose your action:")
    label.pack(pady=10)

    cooperate_button = tk.Button(player1_window, text="Cooperate", command=lambda: on_decision(COOPERATE))
    cooperate_button.pack(side=tk.LEFT, padx=5, pady=5)

    cheat_button = tk.Button(player1_window, text="Cheat", command=lambda: on_decision(CHEAT))
    cheat_button.pack(side=tk.LEFT, padx=5, pady=5)

    player2_window = tk.Toplevel()
    player2_window.title(f"{other_player.name}'s Decision")

    label = tk.Label(player2_window, text=f"{other_player.name}, choose your action:")
    label.pack(pady=10)

    cooperate_button = tk.Button(player2_window, text="Cooperate", command=lambda: on_decision(COOPERATE))
    cooperate_button.pack(side=tk.LEFT, padx=5, pady=5)

    cheat_button = tk.Button(player2_window, text="Cheat", command=lambda: on_decision(CHEAT))
    cheat_button.pack(side=tk.LEFT, padx=5, pady=5)
