class Solution(object):
    def __init__(self):
        self.sols = {}
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        else:
            out = max([self.maxSubArray(nums[:len(nums)//2]),
                       self.maxSubArray(nums[len(nums)//2:]),
                       self.find_max_mid(nums)])
            return out

    def find_max_mid(self, nums):
        max_sum_left = -1e7
        for i in reversed(range(len(nums)//2)):
            if sum(nums[i: len(nums)//2]) > max_sum_left:
                max_sum_left = sum(nums[i: len(nums)//2])
        max_sum_right = -1e-7
        for j in range(len(nums)//2 + 1, len(nums)+1):
            if sum(nums[len(nums)//2: j]) > max_sum_right:
                max_sum_right = sum(nums[len(nums)//2: j])
        return max_sum_left+max_sum_right


# faster O(n) solution
class Solution2:
    def maxSubArray(self, arr):
        cur, ans = 0, 0 # cur is either 0 or sum of the previous elements, ans is the max sum found
        for n in arr:
            cur = max(cur + n, 0)
            ans = max(cur, ans)
        return ans or max(arr)