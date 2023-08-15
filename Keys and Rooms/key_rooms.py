import queue
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        G = {i: l for i, l in enumerate(rooms)}
        dists = {i: False for i in range(n)}
        dists[0] = True
        Q = queue.Queue()
        Q.put(0)
        while not Q.empty():
            u = Q.get()
            for v in G[u]:
                if not dists[v]:
                    dists[v] = True
                    Q.put(v)
        
        return all(dists.values())