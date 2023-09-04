from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while start < end-1:
            mid = (start + end) // 2
            if nums[mid] < nums[start]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            else:
                return nums[start]
        return min(nums[start:end+1])
        