from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    n = len(nums)
    for i in range(n - 1):         # we do two for loops, one starting at the first element and going to the second
        for j in range(i+1, n):    # to last element, and another (j) starting at the second element and going
            if nums[i] == nums[j]: # to the last element 
                return True
    return False


practice = [3, 2, 3, 3, 0, 43, 22, 4, 0]
result = containsDuplicate(nums=practice)
print(result) 

