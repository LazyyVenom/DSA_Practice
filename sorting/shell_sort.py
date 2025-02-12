from typing import List

def sortArray(nums: List[int]) -> List[int]:
    """
    Shell sort algorithm
    Similar to insertion sort uses gap to sort the elements
    O(n^2) time complexity
    """
    n = len(nums)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            gValue = nums[i]
            j = i - gap
            while j >= 0 and nums[j] > gValue:
                nums[j+gap] = nums[j]
                j = j - gap
            nums[j+gap] = gValue
        gap = gap // 2
    return nums