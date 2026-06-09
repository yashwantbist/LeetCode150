#Products of Array Except Self
'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
2 <= nums.length <= 1000
-20 <= nums[i] <= 20
We can use the stored prefix and suffix products to compute the result array
 by iterating through the array and simply multiplying the prefix and suffix 
 products at each index.

'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)          # number of elements in the input array
        output = [1] * n       # result array, initialised to all 1s (neutral for multiplication)

        # ── PASS 1: build prefix products (left to right) 
        prefix = 1             # running product of everything to the LEFT so far
        for i in range(n):
            output[i] = prefix         # store "product of all elements before i"
            prefix *= nums[i]          # now include nums[i] for the next iteration
        # after pass 1, output = [1, 1, 2, 8]
        # output[0]=1 (nothing to left), output[1]=1, output[2]=1×2=2, output[3]=1×2×4=8

        # ── PASS 2: multiply in suffix products (right to left)
        suffix = 1             # running product of everything to the RIGHT so far
        for i in range(n - 1, -1, -1):  # iterate from last index down to 0
            output[i] *= suffix        # multiply the existing prefix by the right-side product
            suffix *= nums[i]          # now include nums[i] for the next (leftward) iteration
        # after pass 2, output = [1×48, 1×24, 2×6, 8×1] = [48, 24, 12, 8]

        return output


solution = Solution()
print(solution.productExceptSelf([1, 2, 4, 6]))   # [48, 24, 12, 8]
print(solution.productExceptSelf([-1, 0, 1, 2, 3])) # [0, -6, 0, 0, 0]