import time
from random import choices

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        else:
            n = len(s)
            d = {}
            for i in range(n):
                d[i] = {}
                for j in range(n):
                    if i==j:
                        d[i][i] = (s[i])
                    else:
                        d[i][j] = ("")
            for l in range(2, n+1):
                for i in range(n - l + 1):
                    j = i + l - 1
                    if s[i] != s[j]:
                        if len(d[i + 1][j]) > len(d[i][j - 1]):
                            d[i][j] = d[i + 1][j]
                        else:
                            d[i][j] = d[i][j - 1]
                    else:
                        if len(d[i + 1][j - 1]) == j-i-1:
                            d[i][j] = s[i] + d[i + 1][j - 1] + s[j]
                        else:
                            if len(d[i + 1][j]) > len(d[i][j - 1]):
                                d[i][j] = d[i + 1][j]
                            else:
                                d[i][j] = d[i][j - 1]
            # print(d)
        return d[0][n-1]


class Solution2:
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        start = 0
        end = 0
        for i in range(len(s)):
            OddStringLength = self.findPalindrome(s, i, i)
            EvenStringLength = self.findPalindrome(s, i, i + 1)
            maxLength = max(OddStringLength, EvenStringLength)
            if (maxLength > end - start):
                end = i + maxLength // 2
                start = i - (maxLength - 1) // 2
        return s[start:end + 1]

    def findPalindrome(self, s, left, right):
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1

start = time.time()
s = Solution()
s2 = Solution2()
s_in = choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10000)
print(s.longestPalindrome(s_in))
print(time.time()-start)