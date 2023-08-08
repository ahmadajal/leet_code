from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ones_rows = [sum(r) for r in grid]
        ones_cols = [sum([grid[r][c] for r in range(m)]) for c in range(n)]
        diff = []
        for i in range(m):
            diff.append([0]*n)
            for j in range(n):
                diff[i][j] = 2*ones_rows[i]+2*ones_cols[j]-n-m
        return diff

s = Solution()
print(s.onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))
