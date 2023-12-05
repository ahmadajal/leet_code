from typing import List
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            res = [nums]
            return res
        for i in range(len(nums)):
            res = res + [[nums[i]] + l_ for l_ in self.permute(nums[:i]+nums[i+1:])]
        return res
