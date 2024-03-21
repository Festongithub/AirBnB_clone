#!/usr/bin/python3

def add_integer(a, b=87):
    """ Adds two integers """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be integer")

    if isinstance(a, float):
        a = int(b)
    if isinstance(b, float):
        b = int(b)

    return a+b
