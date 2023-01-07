# ====Login Section====
# open and read user.txt file
# split the contains where comma+1space present
with open('user.txt', 'r+') as user_text:
    text_lines = user_text.readlines()

# adding text file data into a dictionary
# remove whitespace using .strip()
user_dict = {}  # dictionary
for each_line in text_lines:
    data = each_line.split(',')
    un = data[0].strip()
    pd = data[1].strip()
    user_dict[un] = pd



username = []  # will be used later at 'menu==vm'


login = False
while login == False:

    username_input = input("USERNAME: ")
    username.append(username_input)

    password_input = input("PASSWORD: ")

    # login is true only when both username and password match with user.txt
    if username_input in user_dict:
        if user_dict[username_input] == password_input:
            print("LOGIN SUCCESSFUL")
            login = True
        else:
            print("PASSWORD INCORRECT! TRY AGAIN\n")
            login = False
    else:
        print("USERNAME OR PASSWORD IS NOT VALID. TRY AGAIN\n")
        login = False


while True:
    # main menu list modified
    # user input is converted to lower case.
    # condition added to the username input
    if username[0] == 'admin':
        menu = input('''Select one of the following Options below:
                r - Registering a user
                a - Adding a task
                va - View all tasks
                vm - view my task
                ds - display statistics
                e - Exit
                : ''').lower()

        # Registering a user
        if menu == 'r':
            # user input for registration details
            user_input = input("Enter a new username: ")
            pass_word_input = input("Enter a password: ")
            pass_confirm = input("re-enter your password: ")

            # open user.txt to write the new user info
            # written in the file when password re-entering is correct
            with open('user.txt', 'a+') as user_text:
                if pass_word_input != pass_confirm:
                    print("Password did not match!\n-----BACK TO MAIN MENU-----\n")
                else:
                    user_text.write('\n' + user_input)
                    user_text.write(', ')
                    user_text.write(pass_word_input)
                    print("USER REGISTRATION SUCCESSFUL\n")
                    print("\n-----BACK TO MAIN MENU-----\n")

        elif menu == 'a':
            # user input details
            name_user = input("The task is assigned to ")
            task_title = input("Title of the task is ")
            description = input("Description: ")
            due_date = input("Enter the due date: ")
            current_date = input("enter today's date: ")
            complete = input("Completed?(Yes/No): ")

            # write user input to tasks.txt file
            with open('tasks.txt', 'a+') as task_file:
                task_file.write('\n' + name_user)
                task_file.write(
                    ", " + task_title + ", " + description + ", " + due_date + ", " + current_date + ", " + complete)

        # View all tasks
        elif menu == 'va':
            # open tasks.txt to read its data
            # lines of text made into a list
            # each line stripped to separate list items
            with open('tasks.txt', 'r') as task_file:

                task_list = []
                for line in task_file:
                    line_strip = line.strip()
                    task_list.append(line_strip)

                # items of each task_list item is split where comma+space present
                for item in range(len(task_list)):
                    item_split = task_list[item].split(', ')

                    print(f"\nTask:                 {item_split[1]}"
                          f"\nAssigned to:          {item_split[0]}"
                          f"\nDate assigned:        {item_split[3]}"
                          f"\nDue date:             {item_split[4]}"
                          f"\nTask complete:        {item_split[5]}"
                          f"\nTask Description:"
                          f"\n\t{item_split[2]}")

                print("\n-----BACK TO MAIN MENU-----\n")

        # View Logged-in user's task
        elif menu == 'vm':

            # open tasks.txt to read its data
            # lines of text made into a list
            # each line stripped to separate list items
            with open('tasks.txt', 'r') as task_file:
                task_list = []
                for line in task_file:
                    line_strip = line.strip()
                    task_list.append(line_strip)

                # items in task_list as made into new separate lines
                # each line is added to a new list
                # content of each list is splitter where ', ' present
                # return the details when first item of any split_list match with username
                content_in_list = []
                count = 0
                for items in task_list:
                    split_list = items.split(', ')
                    if split_list[0] == username[0]:  # split_list column 0
                        content_in_list.append(split_list)

                # prints as many tasks as the user has
                for i in content_in_list:
                    print(f"\nTask:                 {i[1]}"
                          f"\nAssigned to:          {i[0]}"
                          f"\nDate assigned:        {i[3]}"
                          f"\nDue date:             {i[4]}"
                          f"\nTask complete:        {i[5]}"
                          f"\nTask Description:"
                          f"\n\t{i[2]}")

                print("\n-----BACK TO MAIN MENU-----\n")

        # Display Statistics
        elif menu == 'ds':
            print("DISPLAY STATISTICS:")
            # counts the total number of users
            with open('user.txt', 'r+') as user_file:
                read_user = user_file.readlines()
                print("Total number of users: ", len(read_user))

            # counts the total number of tasks
            with open('tasks.txt', 'r') as task_file:
                read_task = task_file.readlines()
                print("Total number of tasks: ", len(read_task))

            print("\n-----BACK TO MAIN MENU-----\n")

        # Exit
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        # Wrong selection
        else:
            print("\nTHIS OPTION IS AVAILABLE ONLY TO THE ADMIN\n")


    else:
        menu = input('''Select one of the following Options below:
                a - Adding a task
                va - View all tasks
                vm - view my task
                e - Exit
                : ''').lower()
        # Adding task
        if menu == 'a':
            # user input details
            name_user = input("The task is assigned to ")
            task_title = input("Title of the task is ")
            description = input("Description: ")
            due_date = input("Enter the due date: ")
            current_date = input("enter today's date: ")
            complete = input("Completed?(Yes/No): ")

            # write user input to tasks.txt file
            with open('tasks.txt', 'a+') as task_file:
                task_file.write('\n' + name_user)
                task_file.write(
                    ", " + task_title + ", " + description + ", " + due_date + ", " + current_date + ", " + complete)

        # View all tasks
        elif menu == 'va':
            # open tasks.txt to read its data
            # lines of text made into a list
            # each line stripped to separate list items
            with open('tasks.txt', 'r') as task_file:

                task_list = []
                for line in task_file:
                    line_strip = line.strip()
                    task_list.append(line_strip)

                # items of each task_list item is split where comma+space present
                for item in range(len(task_list)):
                    item_split = task_list[item].split(', ')

                    print(f"\nTask:                 {item_split[1]}"
                          f"\nAssigned to:          {item_split[0]}"
                          f"\nDate assigned:        {item_split[3]}"
                          f"\nDue date:             {item_split[4]}"
                          f"\nTask complete:        {item_split[5]}"
                          f"\nTask Description:"
                          f"\n\t{item_split[2]}")

                print("\n-----BACK TO MAIN MENU-----\n")

        # View Logged-in user's task
        elif menu == 'vm':

            # open tasks.txt to read its data
            # lines of text made into a list
            # each line stripped to separate list items
            with open('tasks.txt', 'r') as task_file:
                task_list = []
                for line in task_file:
                    line_strip = line.strip()
                    task_list.append(line_strip)

                # items in task_list as made into new separate lines
                # each line is added to a new list
                # content of each list is splitter where ', ' present
                # return the details when first item of any split_list match with username
                content_in_list = []
                count = 0
                for items in task_list:
                    split_list = items.split(', ')
                    if split_list[0] == username[0]:  # split_list column 0
                        content_in_list.append(split_list)

                # prints as many tasks as the user has
                for i in content_in_list:
                    print(f"\nTask:                 {i[1]}"
                          f"\nAssigned to:          {i[0]}"
                          f"\nDate assigned:        {i[3]}"
                          f"\nDue date:             {i[4]}"
                          f"\nTask complete:        {i[5]}"
                          f"\nTask Description:"
                          f"\n\t{i[2]}")

                print("\n-----BACK TO MAIN MENU-----\n")

        # Exit
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        # Wrong selection
        else:
            print("\nTHIS OPTION IS AVAILABLE ONLY TO THE ADMIN\n")
