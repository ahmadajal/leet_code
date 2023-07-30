from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr):
            return max(arr)
        else:
            curr_max = max(arr[:k+1])
            if curr_max == arr[0]:
                return arr[0]
            else:
                arr = arr[arr.index(curr_max): ] + arr[0: curr_max]
            
            found = False
            while not found:
                curr_max = max(arr[:k])
                if curr_max == arr[0]:
                    found = True
                else:
                    arr = arr[arr.index(curr_max): ] + arr[0: curr_max]
            return arr[0]