import math
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        op = {'+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: x*y,
            '/': lambda x, y: math.floor(x/y) if x/y >0 else math.ceil(x/y)}
        for s in tokens:
            if s not in operators:
                stack.append(s)
            else:
                y = stack.pop()
                x = stack.pop()
                res = op[s](int(x), int(y))
                stack.append(res)
        return int(stack[0])
