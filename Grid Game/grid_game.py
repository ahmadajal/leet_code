from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        max_points2 = 10**10
        sum_bottom_left = 0
        sum_top_right = 0
        # Where shall the first robot take a step down!
        for i in range(n):
            # Mximum points robot 2 could get.
            if i==0:
                sum_bottom_left = 0
                sum_top_right = sum(grid[0][i+1:])
            else:
                sum_bottom_left = sum_bottom_left + grid[1][i-1]
                sum_top_right = sum_top_right - grid[0][i]
            total = max(sum_bottom_left, sum_top_right)
            if total < max_points2:
                max_points2 = total
        
        return max_points2