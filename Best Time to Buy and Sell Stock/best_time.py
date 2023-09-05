from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        if len(prices) == 1:
            return 0
        best = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                best = max(best, prices[r]-prices[l])
            else:
                l = r
            r = r + 1
        return best


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))

        