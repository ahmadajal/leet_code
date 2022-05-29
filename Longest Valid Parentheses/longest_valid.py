import queue

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        total_max = 0
        for i in range(n):
            stack = queue.LifoQueue()
            num_open=0
            max_len = 0
            for e in s[i:]:
                if e=="(":
                    num_open+=1
                    stack.put("(")
                else:
                    if num_open == 0:
                        break
                    else:
                        stack.get()
                        if stack.empty():
                            max_len = max_len + 2*num_open
                            num_open = 0
            total_max = max(max_len, total_max)
        return total_max