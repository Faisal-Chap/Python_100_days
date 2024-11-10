import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

os.system('cls')
user_cardo = random.choice(cards) 
user_cardt = random.choice(cards)
user_cards = f"[{user_cardo},{user_cardt}]"
print(user_cards)

comp_cardo = random.choice(cards)
comp_cardt = random.choice(cards)
comp_cards = f"[{comp_cardo}, 'X']"
print(comp_cards)

def result(user_total):
    comp_total = comp_cardo + comp_cardt
    if user_total > 21:
        print(f'You Lose  & Dealer other {comp_cardt} ')
    elif user_total < comp_total:
        print(f'You Lose   & Dealer other {comp_cardt} ')
    elif user_total > comp_total:
        print(f'You Won  & Dealer other {comp_cardt} ') 
    elif user_total == comp_total:
        print(f'Draw    & Dealer other {comp_cardt}') 

card_extra = input("Do you need other card 'y' or 'n'   ")
if card_extra == 'y':
    user_total = user_cardo + user_cardt + user_cardt
    user_cardt = random.choice(cards)
    print(f"Extra card {user_cardt} ")
    result(user_total)

elif card_extra == 'n':
    user_total = user_cardo + user_cardt 
    result(user_total)