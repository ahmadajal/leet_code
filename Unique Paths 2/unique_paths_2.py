import numpy as np

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        num_paths = np.zeros((m, n), dtype=int)
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    num_paths[i, j] = 0
                elif i==0 and j==0:
                    num_paths[i, j] = 1
                elif i==0:
                    num_paths[i, j] = num_paths[i, j-1]
                elif j==0:
                    num_paths[i, j] = num_paths[i-1, j]
                else:
                    num_paths[i, j] = num_paths[i-1, j] + num_paths[i, j-1]
        return num_paths[m-1, n-1]




s = Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))