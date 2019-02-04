class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i, n in enumerate(nums):
            if n in d:
                return [d[n], i]
            else:

                d[target-n] = i

s = Solution()
print(s.twoSum([3,2,4], 6))
print([1,2]==[2,1])
d = dict()
d[5] = set([2,3,4])
d[5].append(3)
print(d)
