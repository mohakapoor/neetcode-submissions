class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_profit = 0

        for i in prices:
            min_val = min(i,min_val)
            max_profit = max(i-min_val,max_profit)

        return max_profit