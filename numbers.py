num_list = []
for i in range(3):
    num = int(input("input number: "))
    print(num)
    num_list.append(num)
print(f"list of number entered is: {num_list}")

sum_num = sum(num_list)
print(f"sum of the numbers is {sum_num}")

sub_num = num_list[0] - num_list[1]
print(f"First minus second number = {sub_num}")

mult_num = num_list[2] * num_list[0]
print(f"third multiplied by first = {mult_num}")

sum_by_third = sum(num_list) / num_list[2]
print(f"Sum of numbers divided by the third = {sum_by_third}")




