str_manip = input("enter the sentence: ")

# calculate the length
print("\nlength of the string is: ")
print(len(str_manip))

# find the last letter
print("\nlast letter: ")
print(str_manip[-1])

# replace that letter with @ anywhere in the sentence
replace = str_manip.replace(str_manip[-1], "@")
print("\n")
print(replace)

# last three letters
last_three = str_manip[-3:len(str_manip)]
print("\nlast three letters: ")
print(last_three)

# last three letters in reverse
print("\nin reverse: ")
print(last_three[::-1])


# five-letter word made of first three and last two characters
first_three = str_manip[:3]
print(f"\nFirst three letters: {first_three}")
last_two = str_manip[-2:]
print(f"\nLast two letters: {last_two}")

print("\nfive letter word:")
print(first_three + last_two)

