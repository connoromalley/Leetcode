from typing import List

def twoSum(nums: List[int], target: int) -> List[int]: 
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - value
        if remaining in seen:
            return i, seen[remaining]
        else:
            seen[value] = i 

nums = [3,2,4,5,0]
target = 9
result = twoSum(nums, target)
print(result)