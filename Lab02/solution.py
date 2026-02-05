# solution.py
# Deacon Steiner
# COSC 3020
# Lab02
# 04 February, 2026


def tiler(h: int, w: int):
    side_length = Euclid(h, w)
    number_of_tiles = (h // side_length) * (w // side_length)

    return side_length, number_of_tiles


def Euclid(a: int, b: int) -> int:
    if b == 0:
        return a
    return Euclid(b, a % b)
