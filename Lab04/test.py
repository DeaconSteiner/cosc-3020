# test.py
# Deacon Steiner
# COSC 3020
# Lab04
# 18 February, 2026

from solution import binary_find, dac_find
    

def main():
    # Test 1 - Should return true
    matrix = [[1,4,7,11,15],
              [2,5,8,12,19],
              [3,6,9,16,22],
              [10,13,14,17,24], 
              [18,21,23,26,30]] 
    target = 5
    
    binary_result = binary_find(matrix, target)
    print(f"Binary Search says: {binary_result}")

    dac_result = dac_find(matrix, target)
    print(f"Divide-and-Conquer says: {dac_result}")
    
    # Test 2 - Should return false
    matrix = [[1,4,7,11,15],
              [2,5,8,12,19],
              [3,6,9,16,22],
              [10,13,14,17,24],
              [18,21,23,26,30]]
    target = 20

    binary_result = binary_find(matrix, target)
    print(f"Binary Search says: {binary_result}")

    dac_result = dac_find(matrix, target)
    print(f"Divide-and-Conquer says: {dac_result}")

if __name__ == "__main__":
    main()
