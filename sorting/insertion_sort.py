from typing import List

def sortArray(nums: List[int]) -> List[int]:
    """
    Keeps the left part of the array sorted and inserts the next element in the correct position.
    O(n^2) time complexity
    """
    n = len(nums)
    for i in range(1, n):
        pos = i
        cValue = nums[i]
        while pos > 0 and cValue < nums[pos - 1]:
            nums[pos] = nums[pos - 1]
            pos -= 1
        nums[pos] = cValue
    return nums