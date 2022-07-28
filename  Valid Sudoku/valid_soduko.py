class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for i in range(9)]
        cols = [[] for i in range(9)]
        squares = [[] for i in range(9)]
        for i in range(9):
            for j in range(9):
                try:
                    n = int(board[i][j])
                    if n in rows[i]:
                        return False
                    else:
                        rows[i].append(n)
                    ###
                    if n in cols[j]:
                        return False
                    else:
                        cols[j].append(n)
                    ###
                    s1 = i // 3
                    s2 = j // 3
                    if n in squares[s2 + 3 * s1]:
                        return False
                    else:
                        squares[s2 + 3 * s1].append(n)
                except ValueError:
                    pass
        return True
