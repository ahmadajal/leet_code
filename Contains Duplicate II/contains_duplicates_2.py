from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        countNums = {}

        for i, n in enumerate(nums):
            countNums[n] = countNums.get(n, []) + [i]
            if len(countNums[n]) > 1 and countNums[n][-1]-countNums[n][-2] <= k:
                return True
        return False
        