#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    if (x == 0):
        return (0)
    for num in range(x):
        try:
            if (num == (x - 1) or num == x):
                print(my_list[num])
                i += 1
            else:
                print(my_list[num], end='')
                i += 1
        except (IndexError):
            print("")
            return (i)
    return (i)
