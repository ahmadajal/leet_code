class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_chars = {}
        l, r = 0, 0
        if s == "":
            return 0

        max_len = 0
        while r < len(s):
            curr_chars[s[r]] = curr_chars.get(s[r], 0) + 1
            if curr_chars[s[r]] > 1:
                while l < r:
                    curr_chars[s[l]] -= 1
                    l += 1
                    if curr_chars[s[r]] == 1:
                        break
            max_len = max(max_len, r-l+1)
            r += 1

        return max_len
    

            

        