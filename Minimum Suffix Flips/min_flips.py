class Solution:
    def minFlips(self, target: str) -> int:
        num_flips = 0
        for d in target:
            if d=="0" and num_flips%2==1:
                num_flips += 1
            elif d=="1" and num_flips%2==0:
                num_flips += 1
            else:
                pass
        return num_flips