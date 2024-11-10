'''çalculator app
takes two inputs
performs the action
show result
ask for the continue with answer or new calcu. or exit'''

import os
os.system('cls')


def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 *num2
def divide(num1,num2):
    return num1/num2


operations = {'+':  add, '-': subtract, '*': multiply, '/': divide}
def calculator():
    num1 = int(input('Enter 1st number    '))
    for key in operations:
        print(key)


    user = 'y'
    while user == 'y':
        operation = input("\nChose the operation  ")
        num2 = int(input("Enter next number   "))
        function = operations[operation]
        answer = function(num1,num2)
        print(f'{num1} {operation} {num2}  =  {answer}')

        programe_exit = input(f"Type 'y' to continue calculation with {answer} or 'n' to start new calculation   ")
        if programe_exit == 'y':
            num1 = answer
        elif programe_exit == 'n':
            user = 'n'
            calculator()
        else:
            break

calculator()