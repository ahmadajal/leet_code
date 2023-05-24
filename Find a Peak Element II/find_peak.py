from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        if m==1 or n==1:
            return max(mat)
        else:
            X = [[-1] * (n+2)]
            X = X + [[-1, *r , -1] for r in mat]
            X = X + [[-1] * (n+2)]
            print(X)
            i, j = len(X)//2, len(X[0])//2
            flag = (X[i][j]<X[i-1][j]) or (X[i][j]<X[i+1][j]) or (X[i][j]<X[i][j-1]) or (X[i][j]<X[i][j+1])
            while flag:
                max_val = max([X[i-1][j], X[i+1][j], X[i][j-1], X[i][j+1]])
                if X[i-1][j] == max_val:
                    i = i-1
                elif X[i+1][j] == max_val:
                    i = i+1
                elif X[i][j-1] == max_val:
                    j = j-1
                else:
                    j = j+1
                flag = (X[i][j]<X[i-1][j]) or (X[i][j]<X[i+1][j]) or (X[i][j]<X[i][j-1]) or (X[i][j]<X[i][j+1])
            return [i-1, j-1]