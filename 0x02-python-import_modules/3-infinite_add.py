#!/usr/bin/python3

def main():
    from sys import argv

    """Sum up all command line arguments passed to the python script
    """
    sum = 0
    i = 1
    while i in range(len(argv)):
        sum += int(argv[i])
        i += 1
    print(sum)


if __name__ == '__main__':
    main()
