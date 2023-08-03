def maxProfit(prices):
    minBuyValue = float("inf")
    maxProfitValue = 0
    for price in prices:
        if price < minBuyValue:
            minBuyValue = price
        elif price - minBuyValue > maxProfitValue:
            maxProfitValue = price - minBuyValue
    return maxProfitValue
