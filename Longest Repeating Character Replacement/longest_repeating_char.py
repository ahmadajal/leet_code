from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k > len(s):
            return len(s)
        chars = defaultdict(int)
        l = 0
        ans = 0
        for r in range(len(s)):
            chars[s[r]] += 1
            max_rep = max(chars.values())
            # max_char = [c for c in chars if chars[c]==max_rep][0]
            if r - l + 1 - max_rep <= k:
                ans = max(ans, r - l + 1)
            else:
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    chars.pop(s[l])
                l = l + 1
        return ans