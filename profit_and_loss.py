# Monthly Profit and Loss Account Program

import csv

print("Hello, this is a simple program for calculating profit and loss.")

with open('monthly_profit.csv','w', encoding = 'utf-8', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['Description', 'Date', 'Income', 'Outcome', 'Overall Balance'])

    while True:
        list = []

        dsc = input("Enter the description of the income/expense: ")
        list.append(dsc)
        date = input("Enter the date of the income/expense: ")
        list.append(date)

        c = input("If it was an income, press 'I' \nIf it was an expense, press 'E': ")
        if c == "I":
            inc = input("Amount of the income: ")
            list.append(inc)
            list.append("-")
            list.append(inc)
        elif c == "E":
            exp = input("Amount of the expense: ")
            list.append("-")
            list.append(exp)
            list.append(exp)
        else:
            print("Error. Try again...")


        writer.writerow(list)
        

        e = input("If you are done, press 'Q' \nIf you aren't done yet, press Enter: ")

        if e == "Q":
            break
        else:
            print("")

        
