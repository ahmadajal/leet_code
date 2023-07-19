from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        num_arrays = 0
        # len 1 sub arrays
        num_arrays += len([i for i in nums if i<k])
        # Len 2 or more sub arrays
        start=0
        end=1
        curr_prod = nums[start]
        while end < len(nums) and start < len(nums):
            if curr_prod * nums[end] < k:
                curr_prod = curr_prod * nums[end]
                num_arrays += end-start
                end = end+1
            else:
                # move start one position forward
                curr_prod = curr_prod // nums[start]
                start = start+1
                if start == end:
                    end+=1
                    curr_prod = nums[start]
        return num_arrays
    
