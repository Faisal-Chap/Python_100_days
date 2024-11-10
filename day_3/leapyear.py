''''This programe is going to tell weather the given year is leap or not leap year
1- enter the year
2- for the year to be the leap year it must be fully divisible by 4 i.e year%4+=0
    and not fully divisible to the 100 and 400 as year%100/400!=0'''


year = int(input("Please enter the year: "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("This year is the leap year...")
        else:
            print("This is non-leap year")

    else:
        print("This is a leap year")
        
else:
    print("Your entered year is the non-leap year...")