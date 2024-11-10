'''This game will produce a random number and ask to the user for the input compare the input and print the result
plus has the feature of the easy and hard level. Easy provides the 10 attempts while hard has only the 5 attempts'''

# produce the random number
# ask the user to input the number
# compare function



import os
import random

print("Well-come to Guess the Number Game   ")
rand_no = random.randint(1,100)
print(rand_no)

def level():
    user_level = input("Would you like to play 'easy' or 'hard'   ").lower()
    if user_level == 'easy':
         level = 10
    elif user_level == 'hard':
         level = 5
    return level

g_level = level()
# print(g_level)

def compare(rand_no, user_num):
    if user_num == rand_no:
        print('You Won ...')
    elif user_num < rand_no:
        print("Too low")
    elif user_num > rand_no:
        print("Too high")     

 
def game_logic(rand_no, g_level):
        i = 0
        for i in range(i,g_level):
            # os.system('cls')
            print(f"You have {g_level-i} Remaining Attempts   ")
            user_num = int(input('Please guess a number   '))
            compare(rand_no, user_num)
            if user_num == rand_no:
                 break
            elif i == (g_level-1) and user_num != rand_no:
                 print(f'You lose ...\nYou could not guess {rand_no}')

game_logic(rand_no, g_level)