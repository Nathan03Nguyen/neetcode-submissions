class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = prices[0]

        for s in prices:
            res = max(res, s - low)
            low = min(low, s)
        return res