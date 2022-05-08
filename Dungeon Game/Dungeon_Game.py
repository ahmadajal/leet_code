import numpy as np

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[np.inf for j in range(n+1)] for i in range(m+1)]
        dp[m-1][n-1] = 1 - dungeon[m-1][n-1] if 1 - dungeon[m-1][n-1] > 0 else 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i==m-1 and j==n-1:
                    continue
                else:
                    min_neigh = min(dp[i+1][j], dp[i][j+1])
                    dp[i][j] = min_neigh - dungeon[i][j]
                    if dp[i][j] <= 0:
                        dp[i][j] = 1
        return dp[0][0]