import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(s)
        alpha_num = string.ascii_lowercase + string.digits
        s = [c for c in s if c in alpha_num]

        if len(s) == 0:
            return True

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        
        return True
