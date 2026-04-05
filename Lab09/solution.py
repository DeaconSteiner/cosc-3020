# solution.py
# Deacon Steiner
# COSC 3020
# Lab09
# 04 April, 2026

from typing import List


def sort(nums: List[int]) -> List[int]:

    for i in range(0, len(nums) - 1):
        if i % 2 == 0:
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                continue
        else:
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums
