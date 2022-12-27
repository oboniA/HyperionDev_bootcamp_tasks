num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))
print(f"before swapping, num1: {num1} , num2: {num2}")

# x taken as a temporary variable to store num1
x = num1
num1 = num2
num2 = x
print(f"after swapping, num1: {num1} , num2: {num2}")
