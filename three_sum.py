from collections import Counter

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = []
        s_nums = sorted(nums)
        for i in range(len(nums)-2):
            if i>0 and s_nums[i] == s_nums[i-1]:
                continue
            l, h = i+1, len(nums)-1
            while l<h:
                s = s_nums[i] + s_nums[l] + s_nums[h]
                print(s)
                if s>0:
                    h -= 1
                elif s<0:
                    l += 1
                else:
                    sol.append([s_nums[i], s_nums[l], s_nums[h]])
                    while l<h and s_nums[l] == s_nums[l+1]:
                        l += 1
                    while l<h and s_nums[h] == s_nums[h-1]:
                        h -= 1
                    l += 1
                    h -= 1
        return sol


solution=Solution()
print(solution.threeSum([1,-1,-1,0]))