#!/usr/bin/python -W ignore::DeprecationWarning

from core.cube_utils import scramble
from core.input import getch

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
    k = 'c'
    # q or Q or ctrl+c
    while k != 'q' and k != 'Q' and ord(k) != 3:
        s = scramble(axis['333'], suffixes['333'], 21)
        print ' '.join(s)
        k = getch()


if __name__ == '__main__':
    main()
