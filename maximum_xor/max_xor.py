from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32)[::-1]:
            ans <<= 1
            prefixes = {num >> i for num in nums}
            ans += any(ans^1 ^ p in prefixes for p in prefixes)
        return ans

s = Solution()
print(s.findMaximumXOR([3,4,10,5,25,2,8]))
