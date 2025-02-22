from typing import List

def sortArray(nums: List[int]) -> List[int]:
    count_array = [0] * (max(nums) + 1)
    for num in nums:
        count_array[num] += 1
    
    res = []
    for i, count in enumerate(count_array):
        for _ in range(count):
            res.append(i)

    return res