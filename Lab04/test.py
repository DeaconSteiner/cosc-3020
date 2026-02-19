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
    matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
              [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
              [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
              [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
              [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
              [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
              [91, 92, 93, 94, 95, 96, 97, 98, 99, 100],
              [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
              [111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
              [121, 122, 123, 124, 125, 126, 127, 128, 129, 130],
              [131, 132, 133, 134, 135, 136, 137, 138, 139, 140],
              [141, 142, 143, 144, 145, 146, 147, 148, 149, 150]]
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
