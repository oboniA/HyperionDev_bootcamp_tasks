# user input for total number of total_students in class
total_students = int(input("How many total_students are registering?: "))
print("Total number of total_students is ", total_students)

# creating a file to write in texts
with open('reg_form.txt', 'w+') as text_file:
    # for loop to ask id of each student
    for student in range(total_students):
        id = input("enter Id number: ")
        # user input written to text file
        text_file.write(f"Student {student + 1} : {id} .............."+"\n")
