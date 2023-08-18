from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses==1:
            return [0]
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[1]].append(p[0])
        visited = {node: False for node in range(numCourses)}
        finish = {node: 0 for node in range(numCourses)}
        self.t = 0
        ansc = []

        def dfs(node):
            if visited[node]:
                if node in ansc:
                    return False
                return True
            visited[node] = True
            self.t += 1
            ansc.append(node)
            for child in graph[node]:
                if not dfs(child):
                    return False
            ansc.pop()
            self.t += 1
            finish[node] = self.t
            return True

        for i in range(numCourses):
            ansc = []
            if not dfs(i):
                return []
        print(finish)
        return sorted(finish, key=lambda x: finish[x], reverse=True)
