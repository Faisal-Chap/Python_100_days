import random

# List of lowercase and uppercase letters
letters_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# letters_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of numbers (1 to 9)
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

# You can now combine them or work with them separately

# input the length of the pass
pass_length = int(input("How long the password you want?  "))

# input the number of letter in the pass
num_of_letters = int(input("How many Letters you want in the pass?   "))

#  input the number of digits
num_of_digits = int(input("How many digits you want in your pass?  "))

#  input the number of symbols
num_of_symbols = int(input("How many symbols you want in your pass?  "))

# logic    (running the loop for each stuff (letter, digit, symbol ) and appending that to a list)
password = [ ]
i = 0 
if pass_length >= num_of_digits + num_of_letters + num_of_symbols:
    for i in range (0, num_of_letters):
        rand_letter = random.randint(0,25)
        password.append(letters_lowercase[rand_letter])
    for i in range (0, num_of_digits):
        rand_digit  = random.randint(0,8)
        password.append(numbers[rand_digit])
    for i in range (0, num_of_symbols):
        rand_symbol = random.randint(0,7)
        password.append(symbols[rand_symbol])
else:
    print("Some error try again !!! ")

# from the one list containg first letter then digts and symbols so on making it random using another list 
random_password_list = []

for j in range(0, pass_length):
    rand_value = random.randint(0, pass_length-1)
    random_password_list.append(password[rand_value])

# print(random_password_list)
# converting the list to the string for user use
pass_in_string = ''.join(random_password_list)

print(f"Your Strongest password is here:   {pass_in_string}")