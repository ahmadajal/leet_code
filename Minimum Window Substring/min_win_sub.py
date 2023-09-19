from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if n > m:
            return ""

        t_dict = defaultdict(int)
        for e in t:
            t_dict[e] += 1

        s_dict = {k: 0 for k in t_dict.keys()}
        l = 0
        r = n
        # init s_dict
        for e in s[l:r]:
            if e in t_dict:
                s_dict[e] += 1
        #
        ans = ""
        while r <= m and l<= m-n:
            if s_dict == t_dict:
                if ans == "":
                    ans = s[l:r]
                    if s[l] in s_dict:
                        if s_dict[s[l]] > 0:
                            s_dict[s[l]] -= 1
                    l = l+1
                else:
                    if r-l < len(ans):
                        ans = s[l:r]
                    if s[l] in s_dict:
                        if s_dict[s[l]] > 0:
                            s_dict[s[l]] -= 1
                    l = l+1

            else:
                diffs = [(s_dict[k] - t_dict[k]) >=0 for k in t_dict.keys()]
                if all(diffs):
                    # we have all chars, potentially for some we have more than enough!
                    # make the window smaller
                    if ans == "":
                        ans = s[l:r]
                    elif r-l < len(ans):
                        ans = s[l:r]
                    
                    if s[l] in s_dict:
                        if s_dict[s[l]] > 0:
                            s_dict[s[l]] -= 1
                    l = l+1
                else:
                    # some chars are still missing.
                    # make the window bigger.
                    r = r+1
                    if r<=m:
                        if s[r-1] in s_dict:
                            s_dict[s[r-1]] += 1
        return ans                
