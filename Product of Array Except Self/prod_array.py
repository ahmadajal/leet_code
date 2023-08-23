from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward_prod = [1]*n
        backward_prod = [1]*n
        for i in range(n-2, -1, -1):
            forward_prod[i] = nums[i+1]*forward_prod[i+1]
        for j in range(1, n):
            backward_prod[j] = nums[j-1]*backward_prod[j-1]
            forward_prod[j] = forward_prod[j]*backward_prod[j]
        return forward_prod