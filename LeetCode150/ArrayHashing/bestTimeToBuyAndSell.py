#Best time to buy and sell stock

'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100
Optimal solutions
We are trying to maximize profit = sell - buy. 
If the current i is the sell value, we want to choose the minimum buy value
 to the left of i to maximize the profit. The result will be the 
 maximum profit among all. However, if all profits are negative, 
 we can return 0 since we are allowed to skip doing transaction.

# Algorithm
Keep track of the minimum price seen so far (min_price).
For each price:
Update min_price if the current price is smaller.
Compute the profit if sold today: price - min_price.
Update the maximum profit.
Return the maximum profit (which stays 0 if no profitable transaction exists).
'''
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0


    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

prices = [10, 1, 5, 6, 7, 1]
print("The maximum profit is: ", maxProfit(prices))
