"""

This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.

As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

"""

from random import randint

tateti = [[randint(0,2) for i in range(3)],
          [randint(0,2) for i in range(3)],
          [randint(0,2) for i in range(3)]]

#tablero

print('TaTeTi: ')
print()
print(tateti[0][0:3])
print(tateti[1][0:3])
print(tateti[2][0:3])

#revisión de columnas
if any([all(True if x == 1 else False for x in [tateti[a][0] for a in range(3)]),
       all(True if x == 1 else False for x in [tateti[a][1] for a in range(3)]),
       all(True if x == 1 else False for x in [tateti[a][2] for a in range(3)])]):
       print("Ganó el jugador 1!")
       
if any([all(True if x == 2 else False for x in [tateti[a][0] for a in range(3)]),
       all(True if x == 2 else False for x in [tateti[a][1] for a in range(3)]),
       all(True if x == 2 else False for x in [tateti[a][2] for a in range(3)])]):
       print("Ganó el jugador 2!")
       
#revisión de líneas
if any([all(True if x == 1 else False for x in [tateti[0][:]]),
       all(True if x == 1 else False for x in [tateti[1][:]]),
       all(True if x == 1 else False for x in [tateti[2][:]])]):
       print("Ganó el jugador 1!")
       
if any([all(True if x == 2 else False for x in [tateti[0][:]]),
       all(True if x == 2 else False for x in [tateti[1][:]]),
       all(True if x == 2 else False for x in [tateti[2][:]])]):
       print("Ganó el jugador 2!")
       
#revisión de diagonales
if any([all(True if x == 1 else False for x in [tateti[a][a] for a in range(3)]),
       all(True if x == 1 else False for x in [tateti[-a][-a] for a in range(1,4)])]):
       print("Ganó el jugador 1!")
       
if any([all(True if x == 2 else False for x in [tateti[a][a] for a in range(3)]),
       all(True if x == 2 else False for x in [tateti[-a][-a] for a in range(1,4)])]):
       print("Ganó el jugador 2!")

#else: print("Nadie ganó...")