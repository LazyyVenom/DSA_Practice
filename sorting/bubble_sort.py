from typing import List

def sortArray(nums: List[int]) -> List[int]:
    """
    Sorts the array by comparing adjacent elements and swapping them if they are in the wrong order.    
    O(n^2) time complexity
    """
    n = len(nums)
    for curr_pass in range(n-1,-1,-1):
        for i in range(curr_pass):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    return nums