#This programe is going to calculate the tip for the final bill
'''1- input bill
 2- select tip precentage
 3- enter number of people to split the bill'''
print("\nWellcome to the TIP Calculator app\n\n")


bill = float(input('Please enter your due bill: RS.'))
percentage = float(input("Please Enter the percentage of tip: "))
persons = int(input('Please enter the number of people to split the bill: '))


calculation = ((bill * (percentage/100)) + bill) / persons
print("For every person the due amout will be: RS.", round(calculation,2))