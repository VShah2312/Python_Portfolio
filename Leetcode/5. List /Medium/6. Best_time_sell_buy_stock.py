"""https://www.naukri.com/code360/problems/best-time-to-buy-and-sell-stock_6194560?leftPanelTabValue=PROBLEM"""

#Brute Force: 
def bestTimeToBuyAndSellStock(prices: [int]) -> int:
    maxi = float("-inf")
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            value= prices[j]- prices[i]
            maxi = max(maxi, value)
    return max(maxi, 0)

# TC: O(N^2)
# SC: O(1)


# Optimal: 
def bestTimeToBuyAndSellStock(arr: list[int]) -> int:
    min_price= float("inf")
    max_profit = 0
    for i in range(len(arr)):
        min_price= min(min_price, arr[i])
        max_profit= max(max_profit, arr[i]- min_price)
    return max_profit

# TC: O(N)
# SC: O(1)