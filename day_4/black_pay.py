''''This code will ask for the name of the nobles and then store it to the list
and bring out the random one that will have to pay the bill :( '''


import random


names = input("\n\nPlease enter names as (Ali, Hamza, e.t.c)\n")
upname = names.upper()
names_split = upname.split(', ')
names_list = []
names_list.extend(names_split)

limit = len(names_list) - 1
rand_no = random.randint(0, limit)
name = names_list[rand_no]
print(f"\n\nThe bill payer will be '{name}'\n")

# ali, hamza, adil, ibtihaj, faisal, moshin, zia, chap, bhadur, ilyas