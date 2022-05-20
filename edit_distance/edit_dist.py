class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dist = [[0] * (n + 1) for _ in range(m + 1)]
        dist[0] = list(range(n + 1))
        for i in range(1, m + 1):
            dist[i][0] = i
        #
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # case 1: word1[:-1] -> word2 and delete word1[-1]
                c1 = dist[i - 1][j] + 1
                # case 2: word1 -> word2[:-1] and insert word2[-1]
                c2 = dist[i][j - 1] + 1
                # case 3: word1[:-1] -> word2[:-1]
                if word1[i - 1] == word2[j - 1]:  # last chars match:
                    c3 = dist[i - 1][j - 1]
                else:  # substitute the last chars
                    c3 = dist[i - 1][j - 1] + 1
                ####
                dist[i][j] = min([c1, c2, c3])

        return dist[m][n]