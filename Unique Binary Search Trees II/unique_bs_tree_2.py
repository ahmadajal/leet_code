import itertools
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        all_trees = {i:[] for i in range(n+1)}
        all_trees[0].append(["null"])
        all_trees[1].append([1])
        for i in range(2, n+1):
            # select root
            for j in range(1, i+1):
                left = all_trees[j-1]
                right = all_trees[i-j]
                if i-j == 0:
                    right = [[]]
                combs = list(itertools.product(left, right))
                all_trees[i] += [[j]+l[0]+[e+j if isinstance(e, int) else e for e in l[1]] for l in combs]
        return all_trees[n]

s = Solution()
print(s.generateTrees(3))
