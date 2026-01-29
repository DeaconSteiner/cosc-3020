# solution.py
# Deacon Steiner
# COSC3020
# Lab 01
# 29 January, 2026

from typing import List


def can_meet(interval: List[List[int]]) -> bool:
    """
    Determines whether a person can attend all meetings without overlap.

    Parameters
    ----------
    interval : List[List[int]]
        A list of meeting intervals, of the form [start, end].

    Returns
    ----------
    bool
        True if all meetings can be attended, False otherwise.
    """
    if not interval:
        return True

    interval.sort(key=lambda x: x[0])

    prev = interval[0]
    for meeting in interval[1:]:
        if meeting[0] < prev[1]:
            return False
        prev = meeting
    return True
