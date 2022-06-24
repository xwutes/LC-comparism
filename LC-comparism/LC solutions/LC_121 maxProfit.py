# LC121_maxProfit

def maxProfit(prices) -> int:
    l,r = 0,1
    maxP = 0
    
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP,profit) # here is using current profit comparing with maxP iteratively
        else:
            l = r
        r += 1
    return maxP                     # return value could be set to 0 if none outcome from previous expression


prices = [7,1,4,3,8,1]
#prices = [7,6,4,3,2,1] 
print(maxProfit(prices))