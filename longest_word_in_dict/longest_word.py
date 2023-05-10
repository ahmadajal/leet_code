from typing import List
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words, key=len)
        seen = set([""])
        ans = ""
        for w in words:
            if w[:-1] in seen:
                seen.add(w)
                if len(w) > len(ans):
                    ans = w
                else:
                    if w < ans:
                        ans = w
        return ans
        
