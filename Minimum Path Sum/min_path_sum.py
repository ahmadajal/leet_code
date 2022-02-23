import numpy as np

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid = np.array(grid)
        m, n = grid.shape
        min_path_sum = np.zeros(grid.shape, dtype=int)
        min_path_sum[0] = np.cumsum(grid[0])
        min_path_sum[:, 0] = np.cumsum(grid[:, 0])
        for i in range(1, m):
            for j in range(1, n):
                min_path_sum[i,j] = min(min_path_sum[i-1,j]+grid[i,j], min_path_sum[i, j-1]+grid[i,j])
        return min_path_sum[m-1, n-1]

s = Solution()
print(s.minPathSum([[1,2,3],[4,5,6]]))