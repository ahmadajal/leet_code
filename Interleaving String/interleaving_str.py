
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False
        else:
            m = len(s1)
            n = len(s2)
            grid = [[False] * (n + 1) for _ in range(m + 1)]
            grid[0][0] = True
            for i in range(m + 1):
                for j in range(n + 1):
                    if i + j == 0:
                        continue
                    else:
                        if i == 0:
                            grid[i][j] = (s3[i + j-1] == s2[j-1]) & (grid[i][j - 1])
                        elif j == 0:
                            grid[i][j] = (s3[i + j-1] == s1[i-1]) & (grid[i - 1][j])
                        else:
                            grid[i][j] = ((s3[i + j-1] == s2[j-1]) & (grid[i][j - 1])) | (
                                        (s3[i + j-1] == s1[i-1]) & (grid[i - 1][j]))
            return grid[m][n]

s = Solution()
print(s.isInterleave("aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))