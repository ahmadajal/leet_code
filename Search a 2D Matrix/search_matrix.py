from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m - 1
        while end > start+1:
            if target == matrix[(end+start)//2][0]:
                return True
            elif target > matrix[(end+start)//2][0]:
                start = (end+start)//2
            else:
                end = (end+start)//2
        if (target == matrix[end][0]) or (target == matrix[start][0]):
            return True
        elif target > matrix[end][0]:
            row_index = end
        else:
            row_index = start
        
        i = 0
        j = n - 1
        while j > i+1:
            if target == matrix[row_index][(j+i)//2]:
                return True
            elif target > matrix[row_index][(j+i)//2]:
                i = (j+i)//2
            else:
                j = (j+i)//2
        if (target == matrix[row_index][j]) or (target == matrix[row_index][i]):
            return True
        else:
            return False        

