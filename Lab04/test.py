# test.py
# Deacon Steiner
# COSC 3020
# Lab04
# 18 February, 2026

import time
from solution import binary_find, dac_find
    

def main():
    # Test 1 - Should return true
    matrix = [[1,4,7,11,15],
              [2,5,8,12,19],
              [3,6,9,16,22],
              [10,13,14,17,24], 
              [18,21,23,26,30]] 
    target = 5
    
    # Timing Binary Search
    start_time = time.time()
    binary_result = binary_find(matrix, target)
    binary_time = time.time() - start_time
    print(f"Binary Search says: {binary_result} (Time: {binary_time:.6f} seconds)")

    # Timing Divide-and-Conquer
    start_time = time.time()
    dac_result = dac_find(matrix, target)
    dac_time = time.time() - start_time
    print(f"Divide-and-Conquer says: {dac_result} (Time: {dac_time:.6f} seconds)")
    
    # Test 2 - Should return false
    matrix = [[1,4,7,11,15],
              [2,5,8,12,19],
              [3,6,9,16,22],
              [10,13,14,17,24],
              [18,21,23,26,30]]
    target = 20
    
    # Timing Binary Search
    start_time = time.time()
    binary_result = binary_find(matrix, target)
    binary_time = time.time() - start_time
    print(f"Binary Search says: {binary_result} (Time: {binary_time:.6f} seconds)")

    # Timing Divide-and-Conquer
    start_time = time.time()
    dac_result = dac_find(matrix, target)
    dac_time = time.time() - start_time
    print(f"Divide-and-Conquer says: {dac_result} (Time: {dac_time:.6f} seconds)")

    # Test 3 - Larger matrix for timing demo
    matrix = [[i + j * 1000 + 1 for i in range(1000)] for j in range(1000)]
    target = 42

    # Timing Binary Search
    start_time = time.time()
    binary_result = binary_find(matrix, target)
    binary_time = time.time() - start_time
    print(f"Binary Search says: {binary_result} (Time: {binary_time:.6f} seconds)")

    # Timing Divide-and-Conquer
    start_time = time.time()
    dac_result = dac_find(matrix, target)
    dac_time = time.time() - start_time
    print(f"Divide-and-Conquer says: {dac_result} (Time: {dac_time:.6f} seconds)")

if __name__ == "__main__":
    main()
