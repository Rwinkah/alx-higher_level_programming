#!/usr/bin/python3
def main():
    import hidden_4
    """ Display all names defined in a module"""
    for name in dir(hidden_4):
        if name[0] != '_' and name[1] != '_':
            print(name)


if __name__ == '__main__':
    main()
