from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openC, closedC):
            if closedC == openC == n:
                res.append("".join(stack))
                return None

            if openC < n:
                stack.append("(")
                backtrack(openC+1, closedC)
                stack.pop()

            if closedC < openC:
                stack.append(")")
                backtrack(openC, closedC+1)
                stack.pop()

        backtrack(0, 0)
        return res


# class Solution:
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         parens_of_length = [[""]]
#         if n == 0:
#             return parens_of_length[0]
#         for length in range(1, n + 1):
#             parens_of_length.append([])
#             for i in range(length):
#                 for inside in parens_of_length[i]:
#                     for outside in parens_of_length[length - 1 - i]:
#                         parens_of_length[length].append("(" + inside + ")" + outside)

#         return parens_of_length[n]


s = Solution()
print(s.generateParenthesis(4))