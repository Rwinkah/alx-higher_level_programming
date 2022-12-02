#!/usr/bin/python3
def main():
    """ Display all names defined in a module"""
    for name in dir('hidden-4.pyc'):
        if name[0] != '_' and name[1] != '_':
            print(name)


if __name__ == '__main__':
    main()
