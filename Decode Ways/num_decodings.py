import string
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters =  list(string.ascii_uppercase)
        decode_dict = {"{}".format(i+1): letters[i] for i in range(26)}
        num_ways = [0]*len(s)
        if s[0] != "0":
            num_ways[0] = 1
        else:
            return 0
        for j in range(1,len(s)):
            if s[j-1]+s[j] in decode_dict.keys():
                if j==1 and s[j] != "0":
                    num_ways[j] = 2
                elif j==1 and s[j] == "0":
                    num_ways[j] = 1
                elif j>1 and s[j] == "0":
                    num_ways[j] = num_ways[j-2]
                else:
                    num_ways[j] = num_ways[j - 2] + num_ways[j - 1]
            elif s[j] != "0":
                num_ways[j] = num_ways[j-1]
            else:
                num_ways[j] = 0
        return num_ways[len(s)-1]

s = Solution()
print(s.numDecodings("1320"))