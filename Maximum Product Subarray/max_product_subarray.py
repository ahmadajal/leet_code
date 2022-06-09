import numpy as np


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            min_so_far = max_so_far = res = nums[0]
            for i in range(1, len(nums)):
                temp = max(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)
                min_so_far = min(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)
                max_so_far = temp
                res = max(max_so_far, res)
            return res
#     def maxProduct(self, nums: List[int]) -> int:
#         if len(nums)==1:
#             return nums[0]
#         else:
#             mid = len(nums)//2
#             return max(self.maxProduct(nums[:mid]), self.maxProduct(nums[mid:]), self.maxProductmid(nums, mid))
#     def maxProductmid(self, nums, mid):
#         max_l = -1*np.inf
#         min_l = np.inf
#         max_r = -1*np.inf
#         min_r = np.inf
#         prod_l, prod_r = (1,1)
#         for i in reversed(nums[:mid]):
#             prod_l = prod_l*i
#             if prod_l > max_l:
#                 max_l = prod_l
#             if prod_l < min_l:
#                 min_l = prod_l
#         ##
#         for i in nums[mid:]:
#             prod_r = prod_r*i
#             if prod_r > max_r:
#                 max_r = prod_r
#             if prod_r < min_r:
#                 min_r = prod_r
#         ##
#         return max(max_l*max_r, min_l*min_r)
