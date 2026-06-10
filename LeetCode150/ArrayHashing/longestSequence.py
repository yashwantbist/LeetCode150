#Longest consecutive Sequence
'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which 
each element is exactly 1 greater than the previous element. 
The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
We can consider a number num as the start of a sequence if and only if
 num - 1 does not exist in the given array. We iterate through the array
 and only start building the sequence if it is the start of a sequence. 
This avoids repeated work. We can use a hash set for O(1) lookups by converting the array to a hash set.


'''

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Start a sequence only if num is the beginning
            if num - 1 not in num_set:
                length = 1
                current = num

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest


# Example usage
solution = Solution()

nums = [2, 20, 4, 10, 3, 4, 5]
print("Longest consecutive sequence length:", solution.longestConsecutive(nums))