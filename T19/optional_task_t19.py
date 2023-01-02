# Create text file
# write some content in the file
with open("input.txt", "w+") as text_file:
    text_file.write("This is an optional task for T19.")
    text_file.write("\nThe task is about creating 1 text file "
                    "\nand adding some text.")
    text_file.write("\nThe count the number of characters, words, lines and total number of vowels.")


# open and read file created above
f = open("input.txt", "r+")
read_file = f.read()

# initiate counting variables
count_digit = 0
count_char = 0
count_words = 0
count_vowel = 0
vowels = 'aeiou'


# main code
for item in read_file:
    # digit count
    if item.isdigit():
        count_digit += 1

    # characters count
    if item.isalpha():
        count_char += 1

    # word count
    if item.isspace():
        count_words += 1

    # vowels count
    if item.lower() in vowels:
        count_vowel += 1

print("Total number of digits: ", count_digit)
# punctuation and digits not included

print("Total number of characters: ", count_char)

# always 1 more word than space
print("Total number of words: ", count_words+1)

print("Total number of vowels: ", count_vowel)

f.close()

# count the number of lines
f_2 = open("input.txt", "r+")
lines = f_2.readlines()
total_lines = len(lines)
print("Total lines: ", total_lines)
f_2.close()






