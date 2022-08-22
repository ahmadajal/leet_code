class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        seen_anagrams = {}
        ind = -1
        for s in strs:
            s_u = "".join(sorted(s))
            if s_u in seen_anagrams.keys():
                out[seen_anagrams[s_u]].append(s)
            else:
                ind = ind+1
                seen_anagrams[s_u] = ind
                out.append([s])
        return out