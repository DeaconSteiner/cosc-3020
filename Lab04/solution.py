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

# Divide-and-conquer algorithm
def dac_find(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    r, c = 0, len(matrix[0])-1
    
    while r < len(matrix) and c >= 0:
        if target == matrix[r][c]:
            return True
        elif target < matrix[r][c]:
            c -= 1
        else:
            r += 1

    return False
