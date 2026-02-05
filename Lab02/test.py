# test.py
# Deacon Steiner
# COSC 3020
# Lab02
# 04 February, 2026

from math import e
from this import d

from solution import tiler


def main():
    a = 168
    b = 64

    c = 15
    d = 20

    e = 5
    f = 5

    print(
        f"In order to tile a rectangle with length: {a} and width: {b}, you would need {tiler(a, b)[1]} tiles, with side length: {tiler(a, b)[0]}"
    )

    print(
        f"In order to tile a rectangle with length: {c} and width: {d}, you would need {tiler(c, d)[1]} tiles, with side length: {tiler(c, d)[0]}"
    )

    print(
        f"In order to tile a rectangle with length: {e} and width: {f}, you would need {tiler(e, f)[1]} tiles, with side length: {tiler(e, f)[0]}"
    )


if __name__ == "__main__":
    main()
