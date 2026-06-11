#3 sum
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5

Optimal solution
To efficiently find the j and k pairs, we run the two pointer approach on the elements to the right of index i as the array is sorted. When we run two pointer algorithm, 
consider j and k as pointers (j is at left, k is at right) and target = -nums[i], if the current sum num[j] + nums[k] < target then we need to increase the value of current sum
 by incrementing j pointer. Else if the current sum num[j] + nums[k] > target then we should decrease the value of current sum by decrementing k pointer. 
 How do you deal with duplicates?


Hint 5
When the current sum nums[j] + nums[k] == target add this pair to the result. We can move j or k pointer until j < k and the pairs are repeated.
 This ensures that no duplicate pairs are added to the result.
 
1.Sort the array.
2.Iterate i over each element and treat it as the first element of the triplet.
3.Use two pointers (left and right) for the subarray to the right of i.
4.Skip duplicates for both i and the two-pointer loop to avoid repeated triplets.
'''
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()  # Step 1: sort the array
    res = []

    for i in range(len(nums) - 2):
        # Skip duplicate values for i
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i + 1, len(nums) - 1
        target = -nums[i]  # we want nums[left] + nums[right] == -nums[i]

        while left < right:
            curr_sum = nums[left] + nums[right]

            if curr_sum == target:
                res.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif curr_sum < target:
                left += 1
            else:
                right -= 1

    return res

print(threeSum([-1,0,1,2,-1,-4]))  
print(threeSum([0,1,1]))          
print(threeSum([0,0,0]))           