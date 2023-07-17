from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        if sum(gas) - sum(cost) < 0:
            return -1
        else:
            total = 0
            start = 0
            for i in range(n):
                total += gas[i] - cost[i]
                if total < 0:
                    total = 0
                    start = i+1
            return start
