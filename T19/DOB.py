# Reference:
# BOLD: https://blog.finxter.com/how-to-print-bold-text-in-python/
# https://stackoverflow.com/questions/55251494/i-want-to-create-a-program-that-reads-data-from-a-text-file-and-print-it-out-in

# read file from directory
with open('DOB.txt', 'r+') as birth_dates:
    dob_file = birth_dates.readlines()

    # create empty list to store names and birthdays separately
    names = []
    bdays = []

    for lines in dob_file:
        # split each line as a list
        list_line = lines.split()

        # each first 2 item from every list added in 'names' list
        names.append(list_line[:2])
        # remaining item from every list added in 'bday' list
        bdays.append(list_line[2:])

    # list contents are converted to string
    # Name section
    print("\33[1m" + 'Name' + "\33[0m")
    for i in names:
        print(" ".join(i))

    # Birthday section
    print("\n" + "\33[1m" + 'Birthdate' + "\33[0m")
    for i in bdays:
        print(" ".join(i))
