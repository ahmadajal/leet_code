import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        e = heapq._heappop_max(stones)
        while len(stones) > 0:
            stones[0] = e - stones[0]
            heapq._heapify_max(stones)
            e = heapq._heappop_max(stones)
        return e