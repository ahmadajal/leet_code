class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        min_total = [triangle[0]]
        for r in range(1, len(triangle)):
            min_total.append([])
            for j in range(r+1):
                if j == 0:
                    min_total[r].append(triangle[r][j]+min_total[r-1][j])
                elif j==r:
                    min_total[r].append(triangle[r][j]+min_total[r-1][j-1])
                else:
                    min_total[r].append(min(triangle[r][j]+min_total[r-1][j], triangle[r][j]+min_total[r-1][j-1]))
        return min(min_total[-1])