from functools import lru_cache


class Solution:
    @lru_cache(maxsize=1024)
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)

        if m != n:
            return False
        if not n:
            return True

        if s1 == s2:
            return True
        elif sorted(s1) != sorted(s2):
            return False
        else:
            for i in range(1, n):
                if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (
                        self.isScramble(s1[-i:], s2[:i]) and self.isScramble(s1[:-i], s2[i:])):
                    return True
            return False