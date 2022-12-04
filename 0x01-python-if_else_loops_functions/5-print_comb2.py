#!/usr/bin/python3
def main():
    for i in range(99):
        if i < 10:
            meg = '0' + str(i)
        else:
            meg = str(i)
        print(meg, end=', ')
    print(99)


if __name__ == '__main__':
    main()
