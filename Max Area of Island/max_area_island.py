from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]
        
        def bfs(r, c):
            q = deque([(r,c)])
            area = 0
            while q:
                i, j = q.popleft()
                visited[i][j] = True
                area += 1
                if i-1 >= 0 and grid[i-1][j] == 1 and not visited[i-1][j]:
                    if (i-1, j) not in q:
                        q.append((i-1, j))
                if j-1 >= 0 and grid[i][j-1] == 1 and not visited[i][j-1]:
                    if (i, j-1) not in q:
                        q.append((i, j-1))
                if i+1 < m and grid[i+1][j] == 1 and not visited[i+1][j]:
                    if (i+1, j) not in q:
                        q.append((i+1, j))
                if j+1 < n and grid[i][j+1] == 1 and not visited[i][j+1]:
                    if (i, j+1) not in q:
                        q.append((i, j+1))
            return area
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                else:
                    if not visited[i][j]:
                        max_area = max(bfs(i, j), max_area)

        return max_area
        
        