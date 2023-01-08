# reference: https://www.youtube.com/watch?v=VBQMXW_F5TI

def str_count(str1):
    str_dict = {}
    for i in str1:
        # all key_data are stored in variable called keys
        keys = str_dict.keys()
        if i not in keys:
            str_dict[i] = 1     # value added to keys; initiated
        else:                   # same key repetition
            str_dict[i] += 1    # value incremented

    return str_dict


str_in = input("enter any string: ")
print(str_count(str_in))



