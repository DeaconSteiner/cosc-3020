# solution.py
# Deacon Steiner
# COSC 3020
# Lab09
# 04 April, 2026

import solution


def test(nums):
    print(f"the unsorted array: {nums}")
    print(f"the sorted array: {solution.sort(nums)}")


def main():
    test([3, 5, 2, 1, 6, 4])
    test([6, 6, 5, 6, 3, 8])


if __name__ == "__main__":
    main()
