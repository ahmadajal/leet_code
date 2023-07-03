from typing import List
from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        n = len(answers)
        d = Counter(answers)
        total = n
        for k, v in d.items():
            if k < n and v%(k+1) :
                total = total + k+1 - v%(k+1)
                print(total, k)
            elif k > n:
                total = total - v + k +1 
            else: 
                pass
        return total
            
s = Solution()
print(s.numRabbits([1,0,1,0,0]))