#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str) - 1):
        if ord(str[i]) in range(97, 123):
            msg = chr(ord(str[i]) - 32)
        else:
            msg = str[i]
        print('{}'.format(msg), end='')
    if ord(str[-1]) and ord(str[-1]) in range(97, 123):
        msg = chr(ord(str[-1]) - 32)
    else:
        msg = str[-1]
    print('{}'.format(msg))
