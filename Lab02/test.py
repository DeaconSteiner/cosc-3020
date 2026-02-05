# test.py
# Deacon Steiner
# COSC 3020
# Lab02
# 04 February, 2026

from solution import tiler


def main():
    a = 168
    b = 64

    print(
        f"In order to tile a rectangle with length: {a} and width: {b}, you would need {tiler(a, b)[1]} tiles, with side length: {tiler(a, b)[0]}"
    )


if __name__ == "__main__":
    main()
