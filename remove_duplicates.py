from typing import List

nums = [4,5,5,5,6,7,8] # this algo is only for sorted lists 

def removeDuplicates(nums: List[int]) -> int: 
    j = 1                           # set j to 1 bc we want to be one forward
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]: # if the current isnt equal to the previous, 
            nums[j] = nums[i]      # then overwrite it
            j += 1                #   and move j one forward
    return j
print(nums)
result = removeDuplicates(nums)
print(nums[:result]) # this prints the new list 
print(result) # this prints the length of the list... is that bc the function is set to -> int?