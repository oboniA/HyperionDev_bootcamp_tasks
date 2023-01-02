import math

# user chooses options either Investment or Bond
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n\n"
      "investment  -   to calculate the amount of interest you'll earn on your investment\n"
      "bond        -   to calculate the amount of interest you'll have to pay on a home loan")
options = input(">>").lower()


# if the user selects INVESTMENT
if options == "investment":
    P = float(input("Enter the amount of money you want to deposit "
                    ">> "))

    rate = float(input("Enter the interest rate "
                       ">> "))
    r = rate / 100

    t = int(input("Enter the number of years you plan on investing "
                  ">> "))

    interest = input("Choose the type of interest you want to proceed:\n"
                     "> simple\n"
                     "> compound\n"
                     ">> ").lower()

    # simple interest
    if interest == "simple":
        A = P * (1 + (r * t))
        print("Your total amount after simple interest is as follows: ", A)
    # compound interest
    elif interest == "compound":
        A = P * math.pow((1 + r), t)
        print("Your total amount after compound interest is as follows: ", A)


# if the user selects BOND
if options == "bond":
    P = float(input("Enter the present value of the house: "
                    ">> "))

    rate = float(input("Enter the interest rate "
                       ">> "))
    i = rate / 12

    n = int(input("Enter the number of months over which bond will be repaired "
                  ">> "))

    x = (i * P) / (1 - math.pow((1+i), -n))
    print("Money to replay each month: ", x)