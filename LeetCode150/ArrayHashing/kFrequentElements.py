"""
Top K Frequent Elements
Medium
Topics
Company Tags
Hints
Given an integer array nums and an integer k, 
return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
optimal approach
Use the bucket sort algorithm to create n buckets, 
grouping numbers based on their frequencies from 1 to n. 
Then, pick the top k numbers from the buckets, starting from n down to 1.

Count the frequency of each number using a hash map.
Create buckets: an array where index i contains all numbers that appear exactly i times.
Iterate the buckets from the highest frequency to lowest to collect the top k elements.
"""
from collections import defaultdict, Counter

def topKFrequent(nums, K):
    #step1: count the frequesnies
    freq_map = Counter(nums)

    #step2: Create buckets: index = frequency, value = list of numbers
    n = len(nums)
    #frequencies range from 0 to n
    buckets = [[] for _ in range(n+1)]  

    for num, freq in freq_map.items():
        buckets[freq].append(num)

        #step 3: collect top k frequent elements
        result = []
        #start from the highest frequency
        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result


nums = [1,2,2,3,3,3]
k = 2

print(topKFrequent(nums, k))