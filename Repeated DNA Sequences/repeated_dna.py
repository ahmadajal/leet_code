from collections import defaultdict
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        start = 0
        end = 10
        found = defaultdict(int)
        n = len(s)
        while end <= n:
            found[s[start:end]] += 1
            start += 1
            end += 1
        found = {k:v for k, v in found.items() if v>1}
        return list(found.keys())