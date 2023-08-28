import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        res = max(piles)
        while start <= end:
            k = (end + start) // 2
            hours_req = sum([math.ceil(j/k) for j in piles])
            if hours_req <= h:
                res = min(k, res)
                # k maybe too big
                end = k - 1
            else:
                # k too small
                start = k + 1
        return res
    
s = Solution()

print(s.minEatingSpeed([312884470], 312884469))