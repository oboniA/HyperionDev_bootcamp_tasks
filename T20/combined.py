# references: https://www.scaler.com/topics/python-write-list-to-file/

# open number1 text file to read data
with open('numbers1.txt', 'r+') as file1:
    read_file1 = file1.read()

# open read number2 text file to read data
with open('numbers2.txt', 'r+') as file2:
    read_file2 = file2.read()

# create a new file
# write both files into a new single file called all_numbers
with open('all_numbers.txt', 'w+') as file3:
    file3.write(read_file1 + "\n" + read_file2)

# read the new file
with open('all_numbers.txt', 'r+') as sort_data:
    s_data = sort_data.read()
print("Both files combined: ", s_data)

# convert data from text to string-list type
print("Convert data to a string list(unsorted): ", s_data.split())

# string-type converted to int-type, then sorted from smallest to largest
sorted_d = sorted(s_data.split(), key=int)
print("Sorted data: ", sorted_d)

# sorted data is overwritten in all_numbers.txt
with open('all_numbers.txt', 'w+') as file3:
    for i in sorted_d:
        file3.write(i + "\n")




