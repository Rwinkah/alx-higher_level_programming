#!/usr/bin/python3
def uppercase(str):
    if not str:
        return
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            msg = chr(ord(str[i]) - 32)
        else:
            msg = str[i]
        print('{}'.format(msg), end='')
    print("")
