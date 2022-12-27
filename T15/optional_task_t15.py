# casting the user input number to an int data-type
num = int(input("Enter a number: "))
print(num)
print(type(num))

for i in range(num):
    if num > 10:
        print(num)

if num <= 10:
    print("Sorry, too small")
