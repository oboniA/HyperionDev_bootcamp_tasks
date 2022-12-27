num1 = int(input("enter a number: "))

i = 1
even_num = 0
while i <= num1:
    i += 1
    if i % 2 == 0:
        even_num += 2
        print(even_num)