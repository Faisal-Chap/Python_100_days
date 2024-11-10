'''Rock-Paper-Scisser'''
import random


# instractions
# rock beats scisser
# scisser beats paper
# papaer beats the rock



user_input = input("Please select one 'Rock', 'Paper', 'Scisser' \n").capitalize()
rand_select = random.randint(0,2)
choices = ['Rock','Paper','Scisser']
comp_choice = choices[rand_select]

if user_input == 'Rock' and comp_choice == 'Paper':
    print(f"\n************\nYou LOSE\n           ---You: {comp_choice}        ---Computer: {user_input} ")

elif user_input == 'Paper' and comp_choice == 'Paper':
    print(f"\n************\nTie  \n         ---You: {comp_choice}        ---Computer: {user_input} ")

elif user_input == 'Scisser' and comp_choice == 'Paper':
    print(f"\n************\nYou Won \n          ---You: {user_input}        ---Computer {comp_choice} ")

elif user_input == 'Rock' and comp_choice == 'Rock':
    print(f"\n************\nTIE \n          ---You: {comp_choice}        ---Computer: {user_input} ")

elif user_input == 'Paper' and comp_choice == 'Rock':
    print(f"\n************\nYou WON  \n         ---You: {user_input}        ---Computer: {comp_choice} ")

elif user_input == 'Scisser' and comp_choice == 'Rock':
    print(f"\n************\nYou LOSE \n          ---You: {comp_choice}        ---Computer: {user_input} ")

elif user_input == 'Rock' and comp_choice == 'Scisser':
    print(f"\n************\nYou Won           ---You: {user_input}        ---Computer: {comp_choice} ")

elif user_input == 'Paper' and comp_choice == 'Scisser':
    print(f"\n************\nYou LOSE  \n         ---You: {comp_choice}        ---Computer: {user_input} ")

elif user_input == 'Scisser' and comp_choice == 'Scisser':
    print(f"\n************\nTIE  \n         ---You: {comp_choice}        ---Computer: {user_input} ")
else:
    print('TRY AGAIN !  SOME ERROR :(')