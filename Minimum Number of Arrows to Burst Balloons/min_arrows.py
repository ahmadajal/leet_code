from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        num_arrows = 1
        curr_r = points[0][1]
        for p in points[1:]:
            if p[0] <= curr_r:
                continue
            else:
                num_arrows += 1
                curr_r = p[1]

        return num_arrows
