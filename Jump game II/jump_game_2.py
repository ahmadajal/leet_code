import numpy as np

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_steps_to_end = np.zeros(len(nums), dtype=int)
        for i in reversed(range(len(nums)-1)):
            if nums[i] == 0:
                min_steps_to_end[i] = 1001
            else:
                min_steps_to_end[i] = 1 + min(min_steps_to_end[i+1:i+nums[i]+1])
        return min_steps_to_end[0]


s = Solution()
print(s.jump([2,3,0,1,4]))