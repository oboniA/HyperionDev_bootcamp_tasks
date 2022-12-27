num1 = 23
num2 = 50
num3 = 12

# find the larger number
if num1 > num2:
    print(f"larger number is {num1}")
else:
    print(f"larger number is {num2}")

# odd or even
if num1 % 2 == 0:
    print(f"{num1} is an even number.")
else:
    print(f"{num1} is an odd number.")

# sort
# num1 largest
if (num1 > num2) and (num1 > num3):
    if (num2 > num3):
       print("sorted list: ", num1, num2, num3)
    else:
        print("sorted list: ", num1, num3, num2)

# num2 largest
elif (num2 > num1) and (num2 > num3):
    if (num1 > num3):
        print("sorted list: ", num2, num1, num3)
    else:
        print("sorted list: ", num2, num3, num1)

# num3 largest
else:
    if num2 > num1:
        print("sorted list: ", num3, num1, num2)
    else:
        print("sorted list: ", num3, num2, num1)