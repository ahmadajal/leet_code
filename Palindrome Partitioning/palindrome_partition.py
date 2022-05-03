def is_palindrom(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def dfs(start_ind, path):
            if start_ind >= len(s): self.res.append(path)

            for l in range(len(s) - start_ind):
                if is_palindrom(s[start_ind:start_ind + l + 1]):
                    dfs(start_ind + l + 1, path + [s[start_ind:start_ind + l + 1]])

        self.res = []
        dfs(0, [])
        return self.res
