fav_rest = input("Enter name your favourite resturaunt: ")
int_fav = int(input("enter your favourite number: "))

print(f"Name of the favourite resturaunt is {fav_rest}")
print((f"Favourite number is {int_fav}"))

int_convert = int(fav_rest)
print(int_convert)

"""
ValueError: invalid literal for int() with base 10

fav_rest is a string type with multiple words and alphabets.
it can not be converted to integer type. 
"""

