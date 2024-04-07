from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = sorted(candidates)
        def backtrack(subset, ind, t_):
            if t_ == 0:
                ans.append(subset.copy())
            if t_ <= 0:
                return
            prev = -1
            for i in range(ind, len(candidates)):
                if candidates[i] == prev:
                    continue
                subset.append(candidates[i])
                backtrack(subset, i+1, t_ - candidates[i])
                subset.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return ans
