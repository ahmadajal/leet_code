class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first_ind_available = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[first_ind_available] = nums[i]
                first_ind_available += 1
            else:
                pass
        return first_ind_available
