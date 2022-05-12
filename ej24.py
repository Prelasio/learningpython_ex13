"""
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

"""


def tateti(rango):
    line = ' ---'
    column = '|   '
    for n in range(1,rango+1):
        print(line * rango)
        print(column * (rango+1))
    print(line * rango)

tablero = int(input('De qué tamaño desea el tablero? 3, 8 o 19: '))    
    
tateti(tablero)