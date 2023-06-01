from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        response = [[0]*n for _ in range(n)]
        for q in queries:
            for row_ind in range(q[0], q[2]+1):
                response[row_ind][q[1]] += 1
                if q[3] + 1 < n:
                    response[row_ind][q[3]+1] -= 1
        for i in range(n):
            for j in range(1, n):
                response[i][j] = response[i][j] + response[i][j-1]
        return response