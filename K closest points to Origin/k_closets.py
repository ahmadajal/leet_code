import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [[x[0]**2 + x[1]**2, x[0], x[1]] for x in points]
        heapq.heapify(dists)
        ans = []
        for i in range(k):
            j = heapq.heappop(dists)
            ans.append(j[1:])
        return ans