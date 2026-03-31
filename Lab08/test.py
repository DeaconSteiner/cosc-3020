# test.py
# Deacon Steiner
# COSC 3020
# Lab08
# 30 March, 2026

import solution


def test1():
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n, k = 4, 2
    processed = solution.signal_time(times, n, k)
    if processed == -1:
        print("Signal doesn't reach all nodes")
    else:
        print(f"The signal can be processed in: {processed} units")


def test2():
    times = [[1, 2, 1]]
    n, k = 2, 1
    processed = solution.signal_time(times, n, k)
    if processed == -1:
        print("Signal doesn't reach all nodes")
    else:
        print(f"The signal can be processed in: {processed} units")


def test3():
    times = [[1, 2, 1]]
    n, k = 2, 2
    processed = solution.signal_time(times, n, k)
    if processed == -1:
        print("Signal doesn't reach all nodes")
    else:
        print(f"The signal can be processed in: {processed} units")


if __name__ == "__main__":
    test1()
    test2()
    test3()
