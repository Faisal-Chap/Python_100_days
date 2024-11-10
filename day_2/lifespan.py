#I will tell you the remaining days, weeks, and months in your life sposed you live around 90 years


current_age = input("Please enter how many years you have spent on this earth?")

s_age = 90

r_age = round(90 - int(current_age))
months = r_age * 12
weeks = r_age * 12 * 4.3
days = r_age * 12 * 30

result = f"""\nI got the number of months, weeks, days you left on the Earth\nHere is the data:
\n Remaining Months: {months}\n Remaining Weeks: {weeks} \n Remaining Days: {days}"""
print(result)