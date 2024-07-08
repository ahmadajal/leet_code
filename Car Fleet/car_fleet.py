from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        pair = sorted(pair, key=lambda x: x[0])
        stack = [pair[-1]]
        for p in pair[::-1][1:]:
            stack.append(p)
            t1 = (target-stack[-2][0]) / stack[-2][1]
            t2 = (target-stack[-1][0]) / stack[-1][1]
            if t2 <= t1:
                stack.pop()
            else:
                pass
        return len(stack)
