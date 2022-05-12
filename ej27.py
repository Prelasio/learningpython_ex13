"""
This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 4.

In a previous exercise we explored the idea of using a list of lists as a “data structure” to store information about a tic tac toe game. In a tic tac toe game, the “game server” needs to know where the Xs and Os are in the board, to know whether player 1 or player 2 (or whoever is X and O won).

There has also been an exercise about drawing the actual tic tac toe gameboard using text characters.

The next logical step is to deal with handling user input. When a player (say player 1, who is X) wants to place an X on the screen, they can’t just click on a terminal. So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.

As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board like this:

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3. Then the game would print out

game = [[0, 0, X],
	[0, 0, 0],
	[0, 0, 0]]
And ask Player 2 for their move, printing an O in that place.

"""


gameBoard = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

def boardCheck(gameBoard):
    newlist = []
    for item in gameBoard:
        for value in item:
            newlist.append(value)
    return all(newlist)
            
def displayBoard(gameBoard):
    i = 0
    for item in gameBoard:
        print(gameBoard[i])
        i += 1
def updateBoard(list, player):
    global gameBoard
    gameBoard[list[0]][list[1]] = player
    displayBoard(gameBoard)
    
def getCoord(player):
    global gameBoard
    choice = input(f"{player} elige una posición: fila, columna: ")
    strip = choice.split(",")
    intcoord = [int(x) for x in strip]
    gamecoords = [x - 1 for x in intcoord]
    if type(gameBoard[gamecoords[0]][gamecoords[1]]) is str:
        print("Esa posición ya fue elegida: ")
        altcoords = getCoord(player)
        return altcoords
    return gamecoords

if __name__ == "__main__":
    
    while True:
        print("Las coordenadas del tablero son: ")
        print("1 2 3\n2 \n3")
        ply1x = "x"
        ply2o = "o"
        player1 = "Jugador 1 (x)"
        player2 = "Jugador 2 (o)"
        updateBoard(getCoord(player1), ply1x)
        if boardCheck(gameBoard) is True:
            break
        updateBoard(getCoord(player2), ply2o)
        if boardCheck(gameBoard) is True:
            break
    print("No quedan más movidas posibles!")