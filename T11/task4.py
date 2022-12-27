num = int(input("Enter an integer: "))

if num % 2 == 0 and num % 5 == 0:
    print("Divisible by 2 AND 5")
else:
    print("not divisible by 2 AND 5 ")
    if num % 2 == 0:
        print("Divisible by 2 ONLY")
    elif num % 5 == 0:
        print("Divisible by 5 ONLY")


if num % 2 == 0 or num % 5 == 0:
    print("Divisible by 2 OR 5")
else:
    print("not divisible by 2 OR 5 ")


if num % 2 != 0 or num % 5 != 0:
    print("not divisible by 2 or 5")
else:
    print("divisible by 2 or 5")