import uuid

menu = """-------------
What do you want to do?
1] Host a game
2] Join game
3] See leaderboard
4] Quit
Please type the number for the option:    """

def authenticate():
    # Send request to server

    # After receiving prompt to fill username and password
    name = input("Input name: ")
    input("Input password: ")

    # When succesful, receive Id
    id = uuid.uuid4()

    return name, id

    

def play_game(player1_id, player2_id, decision1, decision2):
    response = requests.post('http://127.0.0.1:5000/play', json={
        'player1_id': player1_id,
        'player2_id': player2_id,
        'decision1': decision1,
        'decision2': decision2
    })
    return response.json()

if __name__ == "__main__":
    
    # name, id = authenticate()

    while True:
        
        menu_input = input(menu)
        print("-------------")
        if (menu_input == "1"):
            pass
        elif (menu_input == "2"):
            pass
        elif (menu_input == "3"):
            pass
        elif (menu_input == "4"):
            print("Disconnecting...")
            break
        else:
            print("Input invalid")