class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno",
             '7': "pqrs", '8': "tuv", '9': "wxyz"}
        l = len(digits)
        if l == 0:
            return []
        else:
            out = list(d[digits[0]])
            for i in range(1, l):
                new = []
                for j in out:
                    for k in list(d[digits[i]]):
                        new.append(j + k)
                out = new
            return out
