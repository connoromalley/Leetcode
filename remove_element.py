from typing import List 

def removeElement(nums: List[int], val: int) -> int:
    index = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index 


nums = [4, 3, 5, 6, 9]
val = 9 
length = removeElement(nums, val)
print(nums[:length])