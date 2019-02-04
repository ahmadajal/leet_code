class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sol = []
        s_nums = sorted(nums)
        for i in range(len(s_nums)-3):
            if i>0 and s_nums[i] == s_nums[i-1]:
                continue
            for j in range(i+1,len(s_nums)-2):
                if j > i+1 and s_nums[j] == s_nums[j - 1]:
                    continue
                l, h = j + 1, len(nums) - 1
                while l < h:
                    s = s_nums[i] + s_nums[j] + s_nums[l] + s_nums[h]
                    if s > target:
                        h -= 1
                    elif s < target:
                        l += 1
                    else:
                        sol.append([s_nums[i], s_nums[j],s_nums[l], s_nums[h]])
                        while l < h and s_nums[l] == s_nums[l + 1]:
                            l += 1
                        while l < h and s_nums[h] == s_nums[h - 1]:
                            h -= 1
                        l += 1
                        h -= 1
        return sol

solution=Solution()
print(solution.fourSum([0,0,0,0,0,0,0,0],0))