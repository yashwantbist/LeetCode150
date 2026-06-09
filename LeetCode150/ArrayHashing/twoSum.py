"""
Two Sum
Easy
Topics
Company Tags
Hints
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
optimal approach 
is we create an empty hash set and run a loop and subtact target - num
and then check if the diff is in hash table or no.

optimal approach
create an hash empty hash table
check i and num in enumerate
get complement = target - num
and if complement is in empty table, return indices of hash table
return indices of num in original table
"""
def twoSum(nums, target):
    #we create an empty dictionary& it will store number : index
    seen = {}

    #run a loop in i and chek for enumerate
    for i, num in enumerate(nums):
        complement = target - num

        # we check the complement in empty set
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


print(twoSum([3,4,5,6],7))