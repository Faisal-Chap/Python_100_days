
import random
import os







hangman_logo = [
    "  _                                              ",
    " | |                                             ",
    " | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __    ",
    " | '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ ",
    " | | | | (_| | | | | (_| | | | | | | (_| | | | |  ",
    " |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|",
    "                     __/ |                      ",
    "                    |___/                       "
]


hangman_words = [
    'apple', 'banana', 'orange', 'grape', 'cherry', 'peach', 'lemon', 'lime', 'melon', 'berry',
    'house', 'garden', 'window', 'door', 'roof', 'kitchen', 'bedroom', 'bathroom', 'garage', 'fence',
    'table', 'chair', 'sofa', 'bed', 'desk', 'lamp', 'shelf', 'drawer', 'mirror', 'carpet',
    'river', 'mountain', 'ocean', 'lake', 'forest', 'desert', 'island', 'valley', 'hill', 'waterfall',
    'book', 'magazine', 'newspaper', 'novel', 'poem', 'story', 'author', 'library', 'chapter', 'page',
    'computer', 'phone', 'tablet', 'keyboard', 'mouse', 'screen', 'printer', 'camera', 'charger', 'router',
    'car', 'bus', 'train', 'plane', 'bicycle', 'motorcycle', 'truck', 'boat', 'subway', 'helicopter',
    'dog', 'cat', 'bird', 'fish', 'horse', 'cow', 'sheep', 'goat', 'chicken', 'rabbit',
    'pencil', 'pen', 'eraser', 'ruler', 'sharpener', 'marker', 'notebook', 'folder', 'scissors', 'glue',
    'pizza', 'burger', 'sandwich', 'pasta', 'rice', 'soup', 'salad', 'steak', 'chicken', 'fish',
    'football', 'basketball', 'tennis', 'golf', 'cricket', 'hockey', 'rugby', 'volleyball', 'baseball', 'soccer',
    'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white',
    'happy', 'sad', 'angry', 'excited', 'nervous', 'scared', 'surprised', 'bored', 'curious', 'tired',
    'doctor', 'teacher', 'engineer', 'artist', 'chef', 'nurse', 'police', 'firefighter', 'lawyer', 'dentist',
    'bread', 'milk', 'cheese', 'butter', 'egg', 'sugar', 'salt', 'pepper', 'oil', 'flour',
    'tree', 'flower', 'grass', 'leaf', 'branch', 'root', 'seed', 'fruit', 'bark', 'wood',
    'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
    'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'weekend', 'holiday', 'vacation',
    'north', 'south', 'east', 'west', 'left', 'right', 'up', 'down', 'forward', 'backward',
    'cold', 'hot', 'warm', 'cool', 'rainy', 'sunny', 'cloudy', 'windy', 'stormy', 'snowy',
    'guitar', 'piano', 'violin', 'drum', 'flute', 'trumpet', 'saxophone', 'harmonica', 'harp', 'clarinet',
    'city', 'village', 'town', 'country', 'capital', 'state', 'nation', 'continent', 'island', 'region',
    'tiger', 'lion', 'elephant', 'zebra', 'giraffe', 'monkey', 'bear', 'wolf', 'fox', 'kangaroo',
    'ice', 'snow', 'rain', 'wind', 'sun', 'cloud', 'fog', 'hail', 'lightning', 'thunder',
    'gold', 'silver', 'bronze', 'diamond', 'ruby', 'emerald', 'pearl', 'crystal', 'gem', 'jade'
]


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']










logo = hangman_logo
for line in logo:
     print(line)

no_of_lives = 6
# getting the random word and input guess
chosen_word = random.choice(hangman_words).lower() 
word = list(chosen_word)
slashes = []
for letter in chosen_word:
    slashes.append('_')


while slashes.count('_') != 0:
    guess = input("\nPlease guess a letter ...").lower()
    os.system('cls')
    for i in range(0, len(chosen_word)):
        if guess == word[i]: 
            slashes[i]= guess
 
    if chosen_word.find(guess) == -1:
            
            no_of_lives -= 1
           
            print('You Lose a Life')
            print(stages[no_of_lives])
            
    if no_of_lives == 0:
        print(f"You Lose ... \nThe word = {chosen_word}")
        break
    elif slashes.count('_') == 0 :
         print('You Won ...')
                     
    print(slashes)






