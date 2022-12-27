# I was unsure about how to execute the conditional statement
# used the YouTube video to try to understand the concept
# Reference Link: https://www.youtube.com/watch?v=AC5ypjFeAoU

def first_task(str1):
    empty_str_1 = []

    for i in range(len(str1)):
        # each even index is upper case
        if i % 2 == 0:
            empty_str_1.append(str1[i].upper())  # reference
        # each odd index is lower case
        else:
            empty_str_1.append(str1[i].lower())  # reference

    return "".join(empty_str_1)


# last time I misread the question so my bad!
# this is the revised version
def second_task(str1):
    empty_str_2 = []
    split_list = str1.split()
    for i in range(len(split_list)):
        # every odd index word is upper case
        if i % 2 != 0:
            empty_str_2.append(split_list[i].upper())
        # every even index word is lower case
        else:
            empty_str_2.append(split_list[i].lower())

    return " ".join(empty_str_2)


my_str = input("Enter a sentence: ")
print(first_task(my_str))
print(second_task(my_str))
