# solution.py
# Deacon Steiner
# COSC 3020
# Lab11
# 20 April, 2026

from typing import List


def move(machines: List[int]) -> int:
    n = len(machines)

    if sum(machines) % n != 0:
        return -1

    target = sum(machines) // n
    balance = 0
    max_moves = 0

    for i in range(n):
        diff = machines[i] - target
        balance += diff
        max_moves = max(max_moves, abs(balance), diff)

    return max_moves
