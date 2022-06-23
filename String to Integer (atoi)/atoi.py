class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        digits = [str(i) for i in range(10)]
        sign = 1
        read = []
        if s[0] == "-":
            sign = -1
        elif s[0] == "+":
            sign = 1
        else:
            if s[0] in digits:
                read.append(s[0])
            else:
                return 0
        for i in range(1, len(s)):
            if s[i] in digits:
                read.append(s[i])
            else:
                break
        ##
        if len(read) == 0:
            return 0
        else:
            num = int(''.join(read)) * sign
            if num > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif num < -2 ** 31:
                return -2 ** 31
            else:
                return num
