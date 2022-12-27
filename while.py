sum_num1 = 0
total_num = 0
while True:
    # counting how many numbers entered
    total_num += 1
    num1 = float(input("enter a number: "))

    # summing the entered numbers
    sum_num1 += num1

    # when number is -1, the loop breaks
    if num1 == -1:
        print("-----reached the end-----\n")
        break

print("Total numbers entered by the user: ", total_num-1)

avg = sum_num1 / total_num-1
print("\nThe average of all the entered numbers is: ", avg)
