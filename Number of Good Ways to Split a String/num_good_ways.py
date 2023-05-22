from collections import defaultdict, Counter

class Solution:
    def numSplits(self, s: str) -> int:
        count = 0
        s_left = defaultdict(int)
        s_right = Counter(s)
        for i in range(0, len(s)-1):
            s_left[s[i]] += 1
            s_right[s[i]] -= 1
            if s_right[s[i]] == 0:
                s_right.pop(s[i])
            if len(s_left) == len(s_right):
                count += 1
        return count
