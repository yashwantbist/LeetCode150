#Container with most water

'''
You are given an integer array heights where heights[i] represents the height of the 
i th bar.

You may choose any two bars to form a container. 
Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4

Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000

optimal approach:
We can use the two pointer algorithm. One pointer is at the start and the other at the end. At each step, we calculate the amount of water using the formula (j - i) * min(heights[i], heights[j]). Then, we move the pointer that has the smaller height value. Can you think why we only move the pointer at smaller height?


Hint 4
If heights[i] is smaller, then any future container using index i will have a smaller width, and its height is still at most heights[i]. So it cannot produce a larger area than the current pair. Therefore, we can safely discard the smaller height and move that pointer inward. The same logic applies when heights[j] is smaller.

Two pointer
Area = (right -left) * min(height[left], height[right])
We start with the widest possible container:

left = 0
right = n - 1

At each step:

Calculate the current area.
Update the maximum area.
Move the pointer with the smaller height inward.
'''
def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h

        max_area = max(max_area, area)

        #move the shorter bar
        if height[left] < height[right]:
            left += 1

        else:
            right -=1
    return max_area

height = [1,7,2,5,4,7,3,6]
print(maxArea(height))
