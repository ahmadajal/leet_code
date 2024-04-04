import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        for _ in range(k):
            e = heapq._heappop_max(nums)
        return e
        