class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        can_jump = [0]*len(nums)
        can_jump[-1] = True
        for i in reversed(range(len(nums)-1)):
            if nums[i] == 0:
                can_jump[i] = False
            else:
                can_jump[i] = sum(can_jump[i+1: i+nums[i]+1]) > 0
        return can_jump[0]

s = Solution()
print(s.canJump([3,2,1,0,4]))
print(sum([True, False, True]))