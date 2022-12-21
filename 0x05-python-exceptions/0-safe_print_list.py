#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    if (x == 0 or my_list == []):
        return (0)
    for num in range(x):
        try:
                print(my_list[num], end='')
                i += 1
        except (IndexError):
            break

    print("")
    return (i)
	
