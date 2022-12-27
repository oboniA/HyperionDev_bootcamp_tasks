num1 = float(input("enter a number less than or equal to 100: "))

while True:
    if num1 <= 100:
        if num1 % 2 == 0:
            print(f"{num1} is an even number. It will be multiplied by 2.")
            mult = num1 * 2
        else:
            print(f"{num1} is an odd number. It will be multiplied by 3.")
            mult = num1 * 3

        print("The multiplication is: ", mult)
        break

    elif num1 > 100:
        print("Number does not fall within the parameter. Please enter again.\n")
        num1 = float(input("enter a number less than or equal to 100: "))
