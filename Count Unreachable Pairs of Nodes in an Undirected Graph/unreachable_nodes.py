from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # build the graph adj matrix
        self.G = defaultdict(list)
        for e in edges:
            self.G[e[0]].append(e[1])
            self.G[e[1]].append(e[0])
        ##
        self.start_finish = {i: [-1, -1] for i in range(n)}
        self.t=0
        for i in range(n):
            if self.start_finish[i][0] < 0:
                self.dfs_visit(i)
        sorted_nodes = sorted(range(n), key=lambda x: self.start_finish[x][0])
        components = []
        num_elements = 0
        curr_f = -1
        for v in sorted_nodes:
            if curr_f < self.start_finish[v][0]:
                components.append(num_elements)
                curr_f = self.start_finish[v][1]
                num_elements = 1
            else:
                num_elements = num_elements+1
        components.append(num_elements)
        all_pairs = 0
        components = components[1:]
        for i in range(len(components)):
            all_pairs += components[i] * (n-components[i])
        return all_pairs//2
    
    def dfs_visit(self, v):
        self.t = self.t+1
        self.start_finish[v][0] = self.t
        for j in self.G[v]:
            if self.start_finish[j][0]<0:
                self.dfs_visit(j)
        self.t = self.t+1
        self.start_finish[v][1] = self.t
    
