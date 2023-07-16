from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        non_overlapping = []
        for i in intervals:
            is_covered=False
            mask = list(range(len(non_overlapping)))
            for ind, j in enumerate(non_overlapping):
                if i[0]<=j[0] and i[1]>=j[1]:
                    mask.remove(ind)
                elif i[0]>=j[0] and i[1]<=j[1]:
                    is_covered=True
                    break
                else:
                    pass
            non_overlapping = [non_overlapping[k] for k in mask]
            if not is_covered:
                non_overlapping.append(i)
        return len(non_overlapping)

