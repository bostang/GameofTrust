import uuid
from datetime import datetime

# Define constants
COOPERATE = 0
CHEAT = 1

# Define the players and their strategies
class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def decide(self):
        return player_input(self.name)

# Function to receive input for decision
def player_input(name):
    while True:
        decision = input(f"{name}, do you choose to cooperate or cheat? ").lower()
        if decision in ['cooperate', 'cheat']:
            match decision:
                case 'cooperate':
                    return COOPERATE
                case 'cheat':
                    return CHEAT
        else:
            print("Invalid choice. Please enter 'cooperate' or 'cheat'.")

# Helper function to convert decision constants back to strings
def decision_to_string(decision):
    return 'cooperate' if decision == COOPERATE else 'cheat'

# Define the possible outcomes
def get_outcome(player1_decision, player2_decision):
    if player1_decision == COOPERATE and player2_decision == COOPERATE:
        return (2, 2)  # Both cooperate
    elif player1_decision == COOPERATE and player2_decision == CHEAT:
        return (0, 3)  # Player 1 cooperates, Player 2 cheats
    elif player1_decision == CHEAT and player2_decision == COOPERATE:
        return (3, 0)  # Player 1 cheats, Player 2 cooperates
    elif player1_decision == CHEAT and player2_decision == CHEAT:
        return (0, 0)  # Both cheat

# Log outcomes of the game
def log_outcome(player1, player2, decision1, decision2, outcome):
    matchtime = datetime.now().isoformat()
    log_entry1 = {
        'timestamp': matchtime,
        'player_id': str(player1.id),
        'player_name': player1.name,
        'player_decision': decision_to_string(decision1),
        'player_points': outcome[0],
    }
    log_entry2 = {
        'timestamp': matchtime,
        'player_id': str(player2.id),
        'player_name': player2.name,
        'player_decision': decision_to_string(decision2),
        'player_points': outcome[1]
    }
    print(f"Log entry 1: {log_entry1}")
    print(f"Log entry 2: {log_entry2}")
    # Append the log entry to a file
    with open('game_log.txt', 'a') as f:
        f.write(str(log_entry1) + '\n')
        f.write(str(log_entry2) + '\n')

# Temporary function to get decision of players
def get_decision():
    return player1.decide(), player2.decide()

# Main function to run the game
def trust_game(player1, player2):
    decision1, decision2 = get_decision()

    print(f"{player1.name} decided to {decision_to_string(decision1)}")
    print(f"{player2.name} decided to {decision_to_string(decision2)}")

    outcome = get_outcome(decision1, decision2)
    print(f"Outcome: {player1.name} gets {outcome[0]} points, {player2.name} gets {outcome[1]} points")

    log_outcome(player1, player2, decision1, decision2, outcome)

# Example usage
if __name__ == "__main__":
    # Create players with their names
    player1 = Player("Player 1", uuid.uuid4())

    player2 = Player("Player 2", uuid.uuid4())

    # Run the game
    trust_game(player1, player2)
