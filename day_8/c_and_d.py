import os

logo = '''
               ██████   ██  ██████   ██   ██  ███████  ██████  
              ██        ██  ██   ██  ██   ██  ██       ██   ██ 
              ██        ██  ██████   ███████  █████    ██████  
              ██        ██  ██       ██   ██  ██       ██   ██ 
               ██████   ██  ██       ██   ██  ███████  ██   ██ 
                                                                                     
'''
code = '''
                               ██████  ██████  ██████  ███████ 
                              ██      ██    ██ ██   ██ ██      
                              ██      ██    ██ ██   ██ █████   
                              ██      ██    ██ ██   ██ ██      
                               ██████  ██████  ██████  ███████                        
'''
decode = '''
               ██████  ███████  ██████  ██████  ██████  ███████ 
               ██   ██ ██      ██      ██    ██ ██   ██ ██      
               ██   ██ █████   ██      ██    ██ ██   ██ █████   
               ██   ██ ██      ██      ██    ██ ██   ██ ██      
               ██████  ███████  ██████  ██████  ██████  ███████                                                                                                   
'''
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's',' ', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


#start
def code_it(user_text, code_shift):
    new_text = ''
    for letter in user_text: 
        position = letters.index(letter)
        new_position = position + code_shift
        new_text += letters[new_position]
    os.system('cls')
    print(logo)
    print(code)
    print(f'\nYour Encoded text is here ↓ ↓ ↓ \n\n---   {new_text}')

def decode_it (user_text, code_shift):
    new_text = ''
    for letter in user_text:
        position = letters.index(letter)
        new_position = position - (code_shift)
        new_text += letters[new_position]
    os.system('cls')
    print(logo)
    print(decode)
    print(f'\nYour Decoded text is here ↓ ↓ ↓ \n\n---   {new_text}')


value = True
while value is True:
    os.system('cls')
    print(logo)
    ask1 = input("Do you want to 'Code' or 'Decode' ?   ").lower()
    os.system('cls')
    if ask1 == 'code':
        print(logo)
        print(code)
        text = input('Please Enter the text to Code ...   ').lower()
        shift = int(input('\nPlease enter the Shift (1-9) to Code ...   '))
        code_it(user_text=text, code_shift=shift)
    elif ask1 == 'decode':
        print(logo)
        print(decode)
        text = input('Please Enter the text to Decode ...   ').lower()
        shift = int(input('\nPlease enter the Shift to Decode ...   '))
        decode_it(user_text=text, code_shift=shift)
    ask2 = int(input("\n\n\nDo you want to 'Exit = 0' or 'Run again = 1' ?   "))
    if ask2 == 0:
        print("\nGood Luck !!!\n\n")
        break
    elif ask2 == 1:
        value == 0
        






