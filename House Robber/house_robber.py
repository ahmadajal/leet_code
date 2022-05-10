class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        sols = [0] * (n + 1)
        sols[1] = nums[0]
        for i in range(2, n + 1):
            sols[i] = max(sols[i - 2] + nums[i - 1], sols[i - 1])
        return sols[-1]
