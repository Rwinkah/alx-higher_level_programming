#!/usr/bin/python3
def main():
    for i in range(99):
        print('{:02d}'.format(i), end=', ')
    print(99)


if __name__ == '__main__':
    main()
