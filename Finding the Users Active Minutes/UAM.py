from typing import List

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        answer = [0] * k
        uam = {}
        for u_id, t in logs:
            if u_id in uam.keys():
                prev_len = len(uam[u_id])
                uam[u_id].add(t)
                if prev_len < len(uam[u_id]):
                    answer[prev_len-1] -= 1
                    answer[len(uam[u_id])-1] += 1
            else:
                uam[u_id] = set([t])
                answer[0] += 1

        return answer
            