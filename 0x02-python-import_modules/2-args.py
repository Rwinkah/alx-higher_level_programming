#!/usr/bin/python3

def main():
    """ caclulate the arguments a program has
    and print out a response accordingly
    """

    from sys import argv
    length = len(argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print(f"1 argument:\n1: {argv[1]}")
    else:
        print(f"{length - 1} arguments:")
        i = 1
        while i < length:
            print(f"{i}: {argv[i]}")
            i += 1


if __name__ == '__main__':
    main()
