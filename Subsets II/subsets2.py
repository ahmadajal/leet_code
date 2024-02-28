from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = [[]]
        last_index = {}
        for n in nums:
            curr_ind = len(res)
            if n in last_index:
                res += [[n] + _ for _ in res[last_index[n]:]]
            else:
                res += [[n] + _ for _ in res]
            last_index[n] = curr_ind
        return res