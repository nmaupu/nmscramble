import random

__author__ = 'nmaupu'


def get_random(m):
    """
    Get a pseudo random integer inside the following set : [0,m-1]
    """
    return random.randint(0, m)


def get_rand_elt(a):
    """
    Get a random element in array a
    :param a: an array of elements
    :return: a random element in given array
    """
    return a[get_random(len(a)-1)]


def scramble(axis, suffixes, length):
    """
    Get a scramble for a cube which is 'length' long.
    :param l: Length of the scramble
    :return: An array corresponding to the scramble containing length elements
    """
    #
    # This algorithm must generate a scramble which :
    #   - Generate a sequence of L, R, U, D, F, B moves such as :
    #      1) The same move does not occur twice in a row
    #      2) There is no sequence such as U D U or more precisely to avoid sequences such as U2 D U2 or U D U'
    #   - For each move, add a suffix for a random amount of that move. So we can generate R, R' or R2
    #
    s = []
    last_axis = -1
    len_axis = len(axis)
    len_suffixes = len(suffixes)

    for i in range(0, length+1):
        finished = False
        last_moves = []
        while not finished:
            row = get_random(len_axis-1)
            col = get_random(len(axis[row])-1)


            # Exact same axis as before, regenerate values
            if (row, col) == last_axis:
                continue

            # Appending this value to the scramble
            s.append(axis[row][col] + get_rand_elt(suffixes))
            finished = True
            last_axis = (row, col)

    return s

