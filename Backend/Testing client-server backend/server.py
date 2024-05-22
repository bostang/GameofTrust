from flask import Flask, request, jsonify
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
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'player1_id': str(player1.id),
        'player1_name': player1.name,
        'player1_decision': decision_to_string(decision1),
        'player1_points': outcome[0],
        'player2_id': str(player2.id),
        'player2_name': player2.name,
        'player2_decision': decision_to_string(decision2),
        'player2_points': outcome[1]
    }
    print(f"Log entry: {log_entry}")
    # Append the log entry to a file
    with open('game_log.txt', 'a') as f:
        f.write(str(log_entry) + '\n')

# Flask application
app = Flask(__name__)

players = {}

@app.route('/register', methods=['POST'])
def register_player():
    name = request.json.get('name')
    player_id = uuid.uuid4()
    player = Player(name, player_id)
    players[str(player_id)] = player
    return jsonify({'player_id': str(player_id)})

@app.route('/play', methods=['POST'])
def play_game():
    player1_id = request.json.get('player1_id')
    player2_id = request.json.get('player2_id')
    decision1 = request.json.get('decision1')
    decision2 = request.json.get('decision2')
    
    player1 = players[player1_id]
    player2 = players[player2_id]

    decision1 = COOPERATE if decision1 == 'cooperate' else CHEAT
    decision2 = COOPERATE if decision2 == 'cooperate' else CHEAT

    outcome = get_outcome(decision1, decision2)
    log_outcome(player1, player2, decision1, decision2, outcome)

    return jsonify({
        'player1_name': player1.name,
        'player1_decision': decision_to_string(decision1),
        'player1_points': outcome[0],
        'player2_name': player2.name,
        'player2_decision': decision_to_string(decision2),
        'player2_points': outcome[1]
    })

if __name__ == '__main__':
    app.run(debug=True)
