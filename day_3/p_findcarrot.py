'''this is the final project of day 3, intended for the purpose of if statements and including the multiple and brached
if else structure...
the concept of this programe will be the rabbit has lost in search of the carrot...
you as a rabbit will reach to a river where you will given two options swim or boat
if swin = LOST
if Boat = FORWARD
then will reach infront of the four doors 
White = Win
Red = lose
Green = lose
'''

print("Hi Fluffy :( \nI know that you are in search of the carrot\nLets go ...")
print("\n\nYou have few choices to find out the Carrot\n")

deci1 = input("You are across the river. Will you 'boat' or 'swim' ?").lower()
if deci1 == 'swim':
    deci2 = input("Welldone !!! you now are infront of the three doors of your luck\nSelect one 'White' 'Red' 'Green' ").lower()
    if deci2 == 'white':
        print('Hurrah! You won the game ...')
    else:
        print('You LOSE')
else:
    print("You LOSE")
