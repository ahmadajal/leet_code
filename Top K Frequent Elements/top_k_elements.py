from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}
        for n in nums:
            count_nums[n] = 1 + count_nums.get(n, 0)
        
        count_nums_reversed = {}
        for key, v in count_nums.items():
            count_nums_reversed[v] = count_nums_reversed.get(v, []) + [key]

        ans = []
        print(count_nums_reversed)

        for c in range(len(nums), 0, -1):
            if c in count_nums_reversed:
                ans = ans + count_nums_reversed[c]
            
            if len(ans) >= k:
                break

        return ans[:k]
    
        