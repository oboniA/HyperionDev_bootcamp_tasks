start = int(input("What year do you want to start with?: "))
years = int(input("How many years do you want to check?: "))

for i in range(start, (start+years)+1):
    if i % 4 == 0:
        print(f"{i} is a leap year.")
    else:
        print(f"{i} isn't a leap year.")
