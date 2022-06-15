
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) <= 3:
            return max(nums)
        nums1 = nums[1:]
        sols1 = [0] * len(nums1)
        sols1[0] = nums1[0]
        sols1[1] = max(nums1[0], nums1[1])
        for i in range(2, len(nums1)):
            sols1[i] = max(sols1[i - 2] + nums1[i], sols1[i - 1])
        ###
        nums2 = nums[:-1]
        sols2 = [0] * len(nums2)
        sols2[0] = nums2[0]
        sols2[1] = max(nums2[0], nums2[1])
        for i in range(2, len(nums2)):
            sols2[i] = max(sols2[i - 2] + nums2[i], sols2[i - 1])

        return max(sols1[-1], sols2[-1])