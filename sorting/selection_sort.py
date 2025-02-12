from typing import List

def selection_sort(nums: List[int]) -> List[int]:
    """
    Finds the smallest element in the unsorted part and swaps it with the first unsorted element,
    reducing the unsorted portion one by one.
    O(n^2) time complexity
    """
    len_nums = len(nums)
    for i in range(len_nums):
        curr_low_idx = i
        for j in range(i, len(nums)):
            if nums[j] < nums[curr_low_idx]:
                curr_low_idx = j

        nums[i], nums[curr_low_idx] = nums[curr_low_idx], nums[i]

    return nums
