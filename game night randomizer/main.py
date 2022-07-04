import random


def gameOfThrones():
    houses = ["Stark", "Lanniser", "Baratheon", "Greyjoy", "Tyrell", "Martell"]
    players = []
    # 5 Players: Remove Martell
    # 4 Players: Remove Martell + Tyrell
    # 3 Players: Remove Martell + tyrell + Greyjoy

    plNum = input("How many players (3-6)?")
    n = int(plNum)
    while (n < 3) or (n > 6):
        plNum = input("Please enter a player number between 3 and 6: ")
        n = int(plNum)
    else:
        gameHouses = houses[:n]
   
    Spaces(1)
    for p in range(n):
        players.append(input("Player " + str(p + 1) + " name? "))
 
    Spaces(1)
    for p in players:
        housePick = random.choice(gameHouses)
        gameHouses.remove(housePick)
        print(p + " plays " + housePick)
        


def anyGame():
    players = []
    options = []

    plNum = input("How many players? ")
    n = int(plNum)
    Spaces(1)
    opNum = input("How many options can a player choose from? ")
    o = int(opNum)
    Spaces(1)
    for p in range(n):
        players.append(input("Player " + str(p + 1) + " name? "))
    Spaces(1)
    for s in range(o):
        options.append(input("Option " + str(s + 1) + ": "))
    Spaces(1)
    for p in players:
        selectOption = random.choice(options)
        print(p + " plays " + selectOption)
        options.remove(selectOption)


def userPickGames(games):
    print("Please select a game:")

    for idx, element in enumerate(games):
        print("{}) {}".format(idx + 1, element))

    i = input("Select a game: ")

    while not (0 < int(i) <= len(games)):
        i = input("Please enter a valid number: ")
    else:
        return int(i) - 1


def Spaces(lines):
    for x in range(lines):
        print("")


games = ["Game of Thrones", "Any Game"]
gameSelect = userPickGames(games)
print("You have selected " + games[gameSelect])
Spaces(2)
if gameSelect == 0:
    gameOfThrones()
elif gameSelect == 1:
    anyGame()
else:
    print("Something went wrong")

Spaces(2)
print("Good Luck!")


