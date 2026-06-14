#Trapping Rain Water

'''
You are given an array of non-negative integers height which 
represent an elevation map. Each value height[i] represents the height of a bar,
 which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:
Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
Constraints:

1 <= height.length <= 1000
0 <= height[i] <= 1000

Optimal solutions:
We can store the prefix maximum in an array by iterating from left to right and the suffix maximum in another array by iterating from right to left. 
For example, in [1, 5, 2, 3, 4], for the element 3, the prefix maximum is 5, and the suffix maximum is 4. Once these arrays are built,
we can iterate through the array with index i and calculate the total water trapped at each position using the formula: min(prefix[i], suffix[i]) - height[i].

Intuition

For each position i, the water trapped depends on:

The tallest bar on the left
The tallest bar on the right

The water level at index i is:

water[i]=min(leftMax[i],rightMax[i])−height[i]

If the result is negative, we treat it as 0.
'''
def trappedWater(height):
    n = len(height)



    leftMax = [0]* n 
    rightMax = [0] * n

    leftMax[0] = height[0]
    for i in range(1,n):
        leftMax[i] = max(leftMax[i -1], height[i])
    

    rightMax[n-1] = height[n-1]
    for i in range(n-2,-1, -1):
        rightMax[i] = max(rightMax[i + 1], height[i])

    
    water = 0
    for i in range(n):
        water += min(leftMax[i], rightMax[i]) - height[i]

    return water
height = [0,2,0,3,1,0,1,3,2,1]
print(trappedWater(height))