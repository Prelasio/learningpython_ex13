"""
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, 
and print out the results to the screen. I have a .txt file for you, if you want to use it!
"""


with open("ejemplo.txt", "r") as nombres:    
    contar_nombres = dict()
    for line in nombres:
        clean_line = line.replace("\n", "")
        if clean_line in contar_nombres.keys():
            contar_nombres[clean_line] += 1            
        else:
            contar_nombres[clean_line] = 1

    print(contar_nombres)
    