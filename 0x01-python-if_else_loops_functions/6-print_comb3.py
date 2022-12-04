#!/usr/bin/python3
def main():
    for i in range(99):
        if (i // 10) < (i % 10) and i != 89:
            print('{}{}'.format((i // 10), (i % 10)), end=', ')
    print(89)


if __name__ == '__main__':
    main()
