# solution.py
# Deacon Steiner
# COSC 3020
# Lab04
# 18 February, 2026

from typing import List

# binary search helper
def search(arr: List[int], x: int):
    lo, hi = 0, len(arr)-1
    
    while lo <= hi:
        # mid point calc
        mid = lo + (hi - lo) // 2
        
        if x == arr[mid]:
            return True
        elif x < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return False

# Finder algorithm using row-wise binary search
def binary_find(matrix: List[List[int]], target: int) -> bool:
    for row in matrix:
        result = search(row, target)
        if result:
            return True
    return False

