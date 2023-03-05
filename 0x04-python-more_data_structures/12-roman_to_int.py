#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    list_roman = list(roman_string)
    sum_num = 0

    for i in range(len(list_roman)):
        if i == 0:
            sum_num += rom_dict[list_roman[i]]
        elif rom_dict[list_roman[i]] > rom_dict[list_roman[i-1]]:
            sum_num -= 2*rom_dict[list_roman[i-1]]
            sum_num += rom_dict[list_roman[i]]
        else:
            sum_num += rom_dict[list_roman[i]]
    return sum_num
