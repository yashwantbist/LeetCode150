#ContainsDuplicate
"""
Given an integer array nums, return true if any value appears
 more than once in the array, otherwise return false.

 Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
"""
#MY Explanations
"""
my thought is get the array; run a loop and check every num that runs twice
but this will increase time complexity
so, we use hash set or hash map to store the elements we have
already seen. This allow us to check if an element is a duplicate 
in constant time
"""

def containsDuplicate(nums):
    # create an empty set
    seen = set()

    for num in nums:
        # if already in set, duplicate found
        if num in seen:
            return True

        # otherwise add it to the set
        seen.add(num)

    return False

print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,2,4,4]))