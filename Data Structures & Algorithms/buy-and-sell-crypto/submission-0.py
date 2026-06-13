class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = prices[0]
        maxProfit = 0

        for i,val in enumerate(prices):
            if i==0:
                continue
            maxProfitTemp = val - minValue
            maxProfit = max(maxProfit,maxProfitTemp)
            minValue = min(minValue,val)
        return maxProfit
        