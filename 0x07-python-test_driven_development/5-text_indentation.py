"""
module to priny two new lines after encountering '.' or '?'
"""


def text_indentation(text):
    """ Checks for certain conditions before executing """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    txt = 0
    while txt < len(text) and text[txt] == ' ':
        txt += 1

    while txt < len(text):
        print(text[txt], end='')

        if text[txt] == '\n' or text[txt] in '.?:':
            if text[txt] in '.?:':
                print('\n')
            txt += 1
            while txt < len(text) and text[txt] == ' ':
                txt += 1
            continue
        txt += 1
