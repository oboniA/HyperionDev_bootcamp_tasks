age = int(input("Enter user age: "))

if age >= 18:
    print("You are old enough!")
elif (age > 16) and (age < 18):
    print("Almost there.")
else:
    print("You're just too young!")