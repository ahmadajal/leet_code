class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_trees = [0] * (n + 1)
        n_trees[0] = 1
        for i in range(1, n + 1):
            # select the root
            for j in range(1, i + 1):
                n_trees[i] += n_trees[j - 1] * n_trees[i - j]

        return n_trees[-1]
