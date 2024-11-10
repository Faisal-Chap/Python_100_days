dic1 = [
    {"name": "Mahar Waqar", "followers": 947200, "description": "Shares aesthetic visuals and popular music duets."},
    {"name": "Aiza Khan", "followers": 935300, "description": "Comedy and lifestyle influencer."},
    {"name": "Noor Hassan", "followers": 933900, "description": "Lifestyle and relatable content creator."},
    {"name": "Syed Shahzeb", "followers": 913200, "description": "Known for comedic and social commentary videos."},
    {"name": "Ayesha Khan", "followers": 910100, "description": "Popular for her lip-syncs and beauty content."},
    {"name": "Abiha Naqvi", "followers": 917200, "description": "Fashion and lifestyle influencer."},
    {"name": "Shah Jahan", "followers": 928100, "description": "Creates humorous skits and lifestyle content."},
    {"name": "Iconic Navid", "followers": 940300, "description": "Known for unique fashion and comedic videos."},
    {"name": "Talha Khan", "followers": 925000, "description": "Focuses on lifestyle, humor, and trending content."},
    {"name": "Ubbi Jaan", "followers": 921500, "description": "Features humor and daily life content."},
    {"name": "Navid The Star", "followers": 940000, "description": "Navid, known for his entertaining skits, resonates with a diverse audience."},
    {"name": "Sehar Khan", "followers": 940000, "description": "Sehar Khan posts lifestyle and comedic content that connects well with younger viewers."},
    {"name": "Maryam Ali", "followers": 950000, "description": "Maryam Ali creates content around relatable family and cultural topics."},
    {"name": "Talha Khan", "followers": 930000, "description": "Talha Khan's humorous videos often focus on everyday struggles and are widely popular."},
    {"name": "Muna Rajput", "followers": 920000, "description": "Muna Rajput's lip-sync videos and skits are quite popular for their relatability."},
    {"name": "Shah Jahan", "followers": 930000, "description": "Shah Jahan focuses on motivational content and short skits that inspire viewers."},
    {"name": "Lishay", "followers": 950000, "description": "Known for her lip-sync videos, Lishay connects well with a younger audience."},
    {"name": "Muazzam King", "followers": 940000, "description": "Muazzam's acting videos showcase relatable drama and comedic moments."},
    {"name": "Phoolllu", "followers": 920000, "description": "Phoolllu creates engaging rural life skits with humorous twists."},
    {"name": "Abiha Naqvi", "followers": 920000, "description": "Abiha focuses on lifestyle and fashion-related TikTok content."}
]


dic2 = [
    {"name": "Ali Jutt", "followers": 10700000, "description": "Known for engaging and humorous videos."},
    {"name": "Mehak Malik", "followers": 13700000, "description": "Famous for her dance and cultural performances."},
    {"name": "Talha Reviews", "followers": 986700, "description": "Creates tech reviews and informative content."},
    {"name": "Khaqan Shahnawaz", "followers": 707700, "description": "Popular lifestyle and fashion influencer."},
    {"name": "Usman Asim", "followers": 10900000, "description": "Posts funny skits and relatable content on everyday situations."},
    {"name": "Nadeem Mubarak", "followers": 11200000, "description": "Known for humorous and light-hearted videos, as well as song covers."},
    {"name": "Sehar Hayat", "followers": 10400000, "description": "Beauty influencer and model with a knack for storytelling."},
    {"name": "Phoolllu", "followers": 10100000, "description": "Shares comedic content and insights into village life."},
    {"name": "Sid Mr. Rapper", "followers": 9700000, "description": "Famous for comedic and music content."},
    {"name": "Queen", "followers": 948200, "description": "Known for lifestyle and relatable content."},
    {"name": "Jannat Mirza", "followers": 25000000, "description": "Known for her beauty and lifestyle videos, Pakistan's most-followed TikTok star from Faisalabad."},
    {"name": "Kanwal Aftab", "followers": 19300000, "description": "Popular for her acting and lip-sync videos, and married to fellow TikTok star Chaudhry Zulqarnain."},
    {"name": "Ali Khan Hyderabadi", "followers": 18100000, "description": "Famous for his unique red glasses and comedic videos, bringing a distinct style to his content."},
    {"name": "Alishba Anjum", "followers": 17800000, "description": "Known for her engaging and relatable lifestyle content, also Jannat Mirza's sister."},
    {"name": "Hoor Mahaveera", "followers": 17000000, "description": "A multi-platform content creator, known for her charm and fashion sense."},
    {"name": "Zulqarnain Sikandar", "followers": 16400000, "description": "Popular for his witty videos and expressions, often collaborating with other creators."},
    {"name": "Dolly (Nousheen Syed)", "followers": 14800000, "description": "A fashion icon who shares beauty tips and trends on TikTok."},
    {"name": "Mehak Malik", "followers": 12700000, "description": "Stage dancer known for her energetic performances and versatile content."},
    {"name": "Zafar Supari", "followers": 11800000, "description": "Businessman and social media personality, famous for his luxurious lifestyle videos."},
    {"name": "Areeka Haq", "followers": 11600000, "description": "Engaging content creator known for her humor and lively personality."},

]


'''this going to have the following featuers
chose the one random name with access to thier followers
chose the 2nd - - - - -  - - - - - - - -
assign them to a and b respectively
ask the user which is higher a or b
go on as long as correct 
finish if the singel gets wrong
count the score
-- remove the asked instance so that no chance of repetition
-- tell if they won the all game ....'''

import random
import os 
score = 0
l_num1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
l_num2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


# function to show the tiktokers and get thier followers
# main game funtion
def game_main():
    os.system('cls')
    '''Asks for the choice and creates random tiktokers ...'''
    random_num1 = random.choice(l_num1)
    random_num2 = random.choice(l_num2)
    # print(random_num1,random_num2)
    random_tiktoker1 = dic1[random_num1]
    random_tiktoker2 = dic2[random_num2]
    # print(random_tiktoker1,random_tiktoker2)
    tk1_n = random_tiktoker1["name"]
    tk1_d = random_tiktoker1["description"]
    tk2_n = random_tiktoker2["name"]
    tk2_d = random_tiktoker2["description"]
    print(f"A:  {tk1_n}\n--{tk1_d}\n\n       VS\n\nB:  {tk2_n}\n--{tk2_d}")
    answer = input(f"\n\nCurrent Score: {score}\n'A' or 'B' ?  ").lower()
    aa = random_tiktoker1["followers"]
    bb = random_tiktoker2["followers"]
    return answer, aa, bb
os.system('cls')
game_on = True
# function to compare the user answer and the orignal values
def compare(answer,aa,bb):
    global score
    global game_on
    # choices = list[aa,bb]
    realans = 'c'
    if aa >= bb:
        realans = 'a'
    elif aa < bb:
        realans = 'b'
    if answer == realans:
        score += 1
    elif answer != realans:
        print(f'\nWrong :(   Your Total Score: {score}\n\n\n')
        game_on = False

while game_on:

    answer, aa, bb = game_main()
    # print(answer,aa,bb)
    compare(answer,aa,bb)