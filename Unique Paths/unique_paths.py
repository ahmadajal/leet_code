import numpy as np

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        sols = np.zeros((m, n), dtype=np.int64)
        sols[0] = 1
        sols[:, 0] = 1
        for i in range(1, m):
            for j in range(1, n):
                sols[i, j] = sols[i-1, j] + sols[i, j-1]
        return sols[m-1, n-1]

s = Solution()
print(s.uniquePaths(10, 10))
