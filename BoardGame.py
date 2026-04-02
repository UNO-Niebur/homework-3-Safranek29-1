# Homework 3 - Board Game System
# Name: Louis Safranek
# Date: 04-02-2026
import random

def loadGameData(filename):
    """Reads game data from a file and returns it as a list."""
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data

def parseData(data):
    """Reads game data from a file and returns it as a dictionary."""
    gameState = {
        "turn": "",
        "players": {},
        "events": {}
    }
    for line in data:
        parts = line.split(": ")
        if parts[0] == "Turn":
            gameState["turn"] = parts[1]
        elif "Player" in parts[1]:
            gameState["players"][parts[1]] = int(parts[0])
        else:
            gameState["events"][int(parts[0])] = parts[1] 

    return gameState

def saveGameData(filename, data):
    with open(filename, "w") as file:
        file.write(f"Turn: {data['turn']}\n")
        for name, position in data["players"].items():
            file.write(f"{position}: {name}\n")
        for space, event in data["events"].items():
            file.write(f"{space}: {event}\n")
        


def displayGame(data):
    """Displays the current game state."""
    print("\nCurrent Game State:")
    for item in data:
        print(item)
def displayBoard(players, events):
    for space in range(1, 31):
        if players["Player1"] == space:
            print("P1", end=" ")
        elif players["Player2"] == space:
            print("P2", end=" ")
        elif players["Player3"] == space:
            print("P3", end=" ")
        elif space in events:
            print(" E", end=" ")
        else:
            print(f"{space:2}", end=" ")
    print()  # new line at the end


def movePlayer(data, filename):
    """Example function to simulate moving a player."""
    # Students will modify this
    name = input("Who is moving? (Player1, Player2, Player3): ")
    name = name.title()
    print(data["players"][name])
    roll = random.randint(1, 6)
    print(f"{name} rolled a {roll}!")
    data["players"][name] = data["players"][name] + roll
    

    if data["players"][name] in data["events"]:
        event = data["events"][data["players"][name]]  # save it first
        if event == "Treasure":
            data["players"][name] += 2
            print(f"{name} landed on Treasure! Moved forward 2 spaces!")
        elif event == "Heal":
            data["players"][name] += 1
            print(f"{name} landed on Heal! Moved forward 1 space!")
        elif event == "Trap":
            data["players"][name] -= 2
            print(f"{name} landed on Trap! Moved back 2 spaces!")

    displayBoard(data["players"], data["events"])   

    if data["players"][name] >= 30:
        print(f"{name} wins!")
        data["players"]["Player1"] = 1
        data["players"]["Player2"] = 1
        data["players"]["Player3"] = 1
        data["turn"] = "Player1"
        saveGameData(filename, data)
    else:
        if data["turn"] == "Player1":
            data["turn"] = "Player2"
        elif data["turn"] == "Player2":
            data["turn"] = "Player3"
        elif data["turn"] == "Player3":
            data["turn"] = "Player1"

        print(f"It is now {data['turn']}'s turn!")
        saveGameData(filename, data)




    
    



def main():
    filename = "events.txt"   # Students can rename if needed

    rawData = loadGameData(filename)
    gameData = parseData(rawData)
    displayBoard(gameData["players"], gameData["events"])
    
    # Example interaction
    movePlayer(gameData, filename)


if __name__ == "__main__":
    main()
