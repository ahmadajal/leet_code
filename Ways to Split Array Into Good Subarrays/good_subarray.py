from typing import List

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 0
        else:
            ans = 1
            first_one = False
            count_zero = 0
            for n in nums:
                if n==0 and not first_one:
                    continue
                elif n==0 and first_one:
                    count_zero += 1
                elif n==1 and not first_one:
                    first_one = True
                else:
                    ans = ans * (count_zero+1)
                    count_zero = 0
        return ans % (10**9 + 7)
