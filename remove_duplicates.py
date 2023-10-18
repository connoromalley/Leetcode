from typing import List

def removeDuplicates(nums: List[int]) -> int: 
    j = 1                           # set j to 1 bc we want to be one forward
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]       # if the current isnt equal to the previous, 
            j += 1                  # then overwrite it and move j one forward
    return j

nums = [4,5,5,5,6,7] # this algo is only for sorted lists 
result = removeDuplicates(nums = nums)
print(result)