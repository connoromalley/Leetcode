def majority_element(nums):
    nums.sort()
    n = len(nums)
    return nums[n//2]

test = [2, 2, 2, 3, 3]

print(majority_element(test))



