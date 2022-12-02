#!/usr/bin/python3
def main():
    """ Import add function from module
    and ensure the  entire module does not run when imported
    """
    from add_0 import add
    a = 1
    b = 2
    c = add(a, b)
    print("{} + {} = {}".format(a, b, c))


if __name__ == '__main__':
    main()
