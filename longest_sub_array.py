from typing import List 

def longest_sub_array(nums: List[int]) -> int:
#this function finds the max sum in an array
    maxSum = float('-inf')
    currentSum = 0
    for i in nums:
        currentSum += 1
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return maxSum

test = [-2,1,-3,4,-1,2,1,-5,4]
result = longest_sub_array(test)
print(result)


