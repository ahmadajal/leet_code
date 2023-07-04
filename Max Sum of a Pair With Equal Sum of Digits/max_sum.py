from typing import List
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for n in nums:
            s = sum([int(d) for d in str(n)])
            d[s].append(n)

        max_sum = -1
        for k, v in d.items():
            if len(v) > 1:
                s = sum(sorted(v)[-2:])
                max_sum = max(s, max_sum)
            else:
                pass
        return max_sum
    

s = Solution()
print(s.maximumSum([18,43,36,13,7]))