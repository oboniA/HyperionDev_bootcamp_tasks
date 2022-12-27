employee = input("Are you a salesperson or a manager?: ")

if employee == "salesperson":
    gross = float(input("What is the gross sale for the month?: "))
    wage = 2000.00 + (gross * 0.08)
    print(f"the salesperson earned R{wage} this month ")
else:
    hours = int(input("How many hours did they work this month?: "))
    wage = 40.00 * hours
    print(f"the {employee} worked for {hours} hours this month and earned R{wage}.")
