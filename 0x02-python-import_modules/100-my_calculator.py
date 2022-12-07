#!/usr/bin/python3
def main():
    from sys import argv, exit
    import calculator_1 as calc
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py a operator b')
        exit(1)
    operator_list = ['+', '-', '*', '/']
    if argv[2] not in operator_list:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    if argv[2] == '+':
        result = calc.add(int(argv[1]), int(argv[3]))
        print('{} + {} = {}'.format(argv[1], argv[3], result))
    if argv[2] == '-':
        result = calc.sub(int(argv[1]), int(argv[3]))
        print('{} - {} = {}'.format(argv[1], argv[3], result))
    if argv[2] == '*':
        result = calc.mul(int(argv[1]), int(argv[3]))
        print('{} * {} = {}'.format(argv[1], argv[3], result))
    if argv[2] == '/':
        result = calc.div(int(argv[1]), int(argv[3]))
        print('{} / {} = {}'.format(argv[1], argv[3], result))


if __name__ == '__main__':
    main()
