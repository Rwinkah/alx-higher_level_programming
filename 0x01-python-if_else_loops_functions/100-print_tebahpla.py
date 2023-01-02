#!/usr/bin/python3

low_z = 122
high_z = 90

for i in range(26):
    if i % 2 == 0:
        print('{}'.format(chr(low_z - i)), end='')
    else:
        print('{}'.format(chr(high_z - i)), end='')
