class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * m for i in range(n)]  # n*m table
        for i in range(m):
            if s[i] == t[0]:
                dp[0][i] = dp[0][i - 1] + 1 if i > 0 else 1
            else:
                dp[0][i] = dp[0][i - 1]
        for j in range(1, n):
            for i in range(j, m):
                if t[j] == s[i]:
                    dp[j][i] = dp[j][i - 1] + dp[j - 1][i - 1]
                else:
                    dp[j][i] = dp[j][i - 1]
        return dp[n - 1][m - 1]
