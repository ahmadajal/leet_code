class Solution:
    def romanToInt(self, s: str) -> int:
        rom2int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        rom2index = {"I":0, "V":1, "X":2, "L":3, "C":4, "D":5, "M":6}
        n = len(s)
        i = 0
        res = 0
        while i < n:
            if i==n-1:
                res = res + rom2int[s[i]]
                i = i+1
            elif s[i] in ["I", "X", "C"] and rom2index[s[i+1]] - rom2index[s[i]] <=2 and rom2index[s[i+1]] - rom2index[s[i]] > 0:
                res = res + rom2int[s[i+1]] - rom2int[s[i]]
                i = i+2
            else:
                res = res + rom2int[s[i]]
                i = i+1
        return res