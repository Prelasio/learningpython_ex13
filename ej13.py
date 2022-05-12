"""
Write a program that asks the user how many Fibonnaci numbers to generate 
and then generates them. Take this opportunity to think about how you can
use functions. Make sure to ask the user to enter the number of numbers in 
the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers 
where the next number in the sequence is the sum of the previous two numbers in 
the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

def fibonacci():
    numero = int(input("Cuantos numeros de Fibonacci precisa:"))
    i = 1
    if numero == 0:
        fibonacci = []
    elif numero == 1:
        fibonacci = [1]
    elif numero == 2:
        fibonacci = [1,1]
    elif numero > 2:
        fibonacci = [1,1]
        while i < (numero - 1):
            fibonacci.append(fibonacci[i] + fibonacci[i-1])
            i += 1
    return fibonacci
print(fibonacci())