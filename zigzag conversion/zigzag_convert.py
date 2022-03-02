import numpy as np
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        else:
            grid = [['']*(len(s)) for _ in range(numRows)]
            grid = np.array(grid)
            s_ind = 0
            grid_c = 0
            while s_ind < len(s):
                if grid_c == 0:
                    if s_ind + numRows < len(s):
                        grid[:, grid_c] = list(s[s_ind:s_ind+numRows])
                    else:
                        grid[:len(s)-s_ind, grid_c] = list(s[s_ind:])
                    s_ind = s_ind + numRows
                else:
                    if s_ind + numRows - 1 < len(s):
                        grid[1:, grid_c] = list(s[s_ind:s_ind+numRows-1])
                    else:
                        grid[1:len(s)-s_ind+1, grid_c] = list(s[s_ind:])
                    s_ind = s_ind+numRows-1
                for i in reversed(range(numRows-1)):
                    if s_ind < len(s):
                        grid[i , grid_c + numRows -1 -i] = s[s_ind]
                        s_ind = s_ind + 1
                    else:
                        break
                grid_c = grid_c + numRows - 1
            out = ''.join([''.join(list(grid[j])) for j in range(numRows)])
            print(grid)
            print(grid_c)
            return out

s = Solution()
print(s.convert("D", 1))
