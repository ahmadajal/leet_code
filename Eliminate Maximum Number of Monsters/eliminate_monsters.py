from typing import List
import math

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_to_reach = [max(1, math.ceil(i/j)) for i,j in zip(dist, speed)]
        time_to_reach = sorted(time_to_reach)
        for i, t in enumerate(time_to_reach):
            if i+1 > t:
                i -= 1
                break
        return i+1
