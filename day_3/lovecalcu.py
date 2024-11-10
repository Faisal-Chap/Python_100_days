

f_name = input("Please enter 1st name:  ").lower()
s_name = input("Please enter 2nd name:  ").lower()
count1 = 0
count2 = 0


count1 += f_name.count("t")
count1 += f_name.count("r")
count1 += f_name.count("u")
count1 += f_name.count("e")
count1 += s_name.count("t")
count1 += s_name.count("r")
count1 += s_name.count("u")
count1 += s_name.count("e")


count2 += f_name.count("l")
count2 += f_name.count("o")
count2 += f_name.count("v")
count2 += f_name.count("e")
count2 += s_name.count("l")
count2 += s_name.count("o")
count2 += s_name.count("v")
count2 += s_name.count("e")



final = f"{count1}{count2}"
print(f"Your score is: {final}%")

finalasint = int(final)
if finalasint <= 10 and finalasint >= 90:
    print("Your are good to go together like hot cakes...")
elif finalasint <= 50 and finalasint >= 40:
    print("You are good to go together...")
else:
    print("Wish for your self...:( ")