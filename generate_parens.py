class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        parens_of_length = [[""]]
        if n == 0:
            return parens_of_length[0]
        for length in range(1, n + 1):
            parens_of_length.append([])
            for i in range(length):
                for inside in parens_of_length[i]:
                    for outside in parens_of_length[length - 1 - i]:
                        parens_of_length[length].append("(" + inside + ")" + outside)

        return parens_of_length[n]


s = Solution()
print(s.generateParenthesis(4))