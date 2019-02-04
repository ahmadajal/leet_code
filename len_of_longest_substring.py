class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_buffer = []
        max_len = 0
        i = 0
        while i < len(s):
            if s[i] not in max_buffer:
                max_buffer.append(s[i])
                i += 1
            else:
                if len(max_buffer) > max_len:
                    max_len = len(max_buffer)
                max_buffer = max_buffer[max_buffer.index(s[i])+1:]
                max_buffer.append(s[i])
                i += 1
            print(max_buffer)
        return max([max_len, len(max_buffer)])

s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))