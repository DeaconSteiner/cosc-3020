# solution.py
# Deacon Steiner
# COSC 3020
# Lab05
# 27 February, 2026

from typing import List


def h_index(citations: List[int]) -> int:
    n: int = len(citations)
    frequency: List[int] = [0] * (n + 1)

    for c in citations:
        if c >= n:
            frequency[n] += 1
        else:
            frequency[c] += 1

    total: int = 0

    for i in range(n, -1, -1):
        total += frequency[i]
        if total >= i:
            return i

    return 0


def main():
    print("Test 1")
    citations = [3, 0, 6, 1, 5]
    print(citations)
    print(f"The h-index for this set is: {h_index(citations)}")

    print("Test 2")
    citations = [1, 3, 1]
    print(citations)
    print(f"The h-index for this set is: {h_index(citations)}")


if __name__ == "__main__":
    main()
