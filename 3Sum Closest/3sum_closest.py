class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_sorted = sorted(nums)
        best_diff_to_target = 1e5
        best_sum = -1e5
        for i in range(len(nums_sorted)):
            new_target = target - nums_sorted[i]
            nums_wo_i = nums_sorted[:i] + nums_sorted[i+1:]
            start = 0
            end = len(nums_wo_i) - 1
            while start < end:
                current_sum = nums_wo_i[start] + nums_wo_i[end]
                if current_sum > new_target:
                    end = end -1
                elif current_sum < new_target:
                    start = start + 1
                else:
                    return new_target + nums_sorted[i]
                if abs(current_sum - new_target) < best_diff_to_target:
                    best_diff_to_target = abs(current_sum - new_target)
                    best_sum = current_sum + nums_sorted[i]
        return best_sum

s = Solution()
print(s.threeSumClosest([-1,2,1,-4], 1))


