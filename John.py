def user_input(user_str):
    incorrect_list = []

    while user_str != 'John':
        incorrect_list.append(user_str)
        user_str = input("Enter your name: ")

        if user_str.lower() == 'john':
            break

    return incorrect_list


user_name = input("Enter your name: ")
print(user_input(user_name))
