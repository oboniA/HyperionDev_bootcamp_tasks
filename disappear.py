# this task was challenging for me. Therefore, had to conduct some reading
# Could not find any suitable video for stripping method
# However, found some solution in stack overflow for replacing method
# reference link: https://stackoverflow.com/questions/60684350/replace-multiple-characters-using-re-sub?noredirect=1&lq=1 ; https://stackoverflow.com/questions/3900054/python-strip-multiple-characters

my_str = input("Enter: ")
split_char = input("Enter characters u want to be disappeared: ")


def disappear_char(new_str):
    for i in split_char:
        if i in new_str:
            new_str = new_str.replace(i, "")

    return new_str


print(disappear_char(my_str))








