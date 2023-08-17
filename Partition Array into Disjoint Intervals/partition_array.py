from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        l_idx = 0
        left_max = nums[0]
        max_so_far = nums[0]
        for idx in range(1, len(nums)-1):
            max_so_far = max(max_so_far, nums[idx])
            if left_max > nums[idx]:
                l_idx = idx
                left_max = max_so_far
        return l_idx+1
