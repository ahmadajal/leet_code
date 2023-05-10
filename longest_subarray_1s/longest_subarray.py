from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if any(nums) or len(nums)>1:
            start = 0
            end = 0
            count = 0
            max_len = 0
            while end < len(nums):
              if nums[end] == 0:
                count += 1
              if count > 1:
                  while count > 1:
                      if nums[start] == 0:
                          count -= 1
                      start += 1
              max_len = max(end-start, max_len)
              end += 1
            return max_len
        else:
            return 0