class Solution:
    def wordBreak(self, s: str, wordDict):
        dp_mem = {}
        dp_mem[len(s)] = [""]
        def wordBreak_recur(s, start):
            if start in dp_mem.keys():
                return dp_mem[start]
            else:
                sents = []
                for j in range(start + 1, len(s)+1):
                    if s[start:j] in wordDict and len(wordBreak_recur(s, j)) > 0:
                        sents = sents + [(s[start:j] + " " + e).strip() for e in wordBreak_recur(s, j)]
                dp_mem[start] = sents
                return sents
        return wordBreak_recur(s, 0)

s = Solution()
print(s.wordBreak(s="catsanddog", wordDict=["cat","cats","and","sand","dog"]))