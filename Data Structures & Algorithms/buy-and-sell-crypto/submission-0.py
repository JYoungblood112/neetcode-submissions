class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        best = -float("inf")

        least = float("inf")

        for i in prices:
            best = max(best, i - least)
            least = min(least, i)
        
        if best < 0:
            return 0
        return best







        