from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(subset, ind):
            for i in range(ind, len(candidates)):
                if sum(subset+[candidates[i]]) == target:
                    res.append(subset+[candidates[i]])
                    continue
                elif sum(subset+[candidates[i]]) > target:
                    continue
                else:
                    dfs(subset+[candidates[i]], i)
            return

        dfs([], 0)
        return res
