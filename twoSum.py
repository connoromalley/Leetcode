# hash table is main algo used

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]: 
    seen = {}
    for i, value in enumerate(nums):             # remember that INDEX COMES FIRST in enumerate... then the value
        remaining = target - value
        if remaining in seen:
            return i, seen[remaining]            # return the current index (i) and the index for this 'remaining' value
        else:                                    # which is already stored in seen
            seen[value] = i 

nums = [3,2,4,5,0]
target = 9
result = twoSum(nums, target)
print(result)
