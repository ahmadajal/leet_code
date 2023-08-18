from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[0]].append(p[1])
        visited = {i: False for i in range(numCourses)}

        def dfs(node):
            if graph[node] == []:
                return True
            
            if visited[node]:
                return False
            else:
                visited[node] = True
                for child in graph[node]:
                    if not dfs(child):
                        return False
                graph[node] = []
                return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True