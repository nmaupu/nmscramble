#!/usr/bin/python -W ignore::DeprecationWarning

from core.utils import scramble

__author__ = 'nmaupu'

suffixes = {
    '333': ["", "2", "'"],
}

axis = {
    '333': [
        ['L', 'R'],
        ['U', 'D'],
        ['F', 'B'],
    ]
}


def main():
    s = scramble(axis['333'], suffixes['333'], 21)
    print ' '.join(s)


if __name__ == '__main__':
    main()
