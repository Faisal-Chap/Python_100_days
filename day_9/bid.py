'''this is going to shose the highest bider of all
- the bidders will be stored in the dictionary
- input the name and the amount 
- funtion to store them all in one dictionary
- funtion to analyze the higher
show the results
'''

import os

dic = {}
def bider(name, amount):
    dic[name] = amount
    max_value = max(dic.values())
    for key, value in dic.items():
        if max_value == value:
            return f'-- {key} Won the Bid ...\n   Congratulaions dear !!! '
    
user = 'yes'
while  user == 'yes':
    os.system("cls")
    name = input("What's your name?   ")
    amount = int(input("How much you want to bid?   "))
    bider(name,amount)
    user = input('Is their any other bidder?  (yes, no) ')
    os.system("cls")
result = bider(name, amount)
print(result)
