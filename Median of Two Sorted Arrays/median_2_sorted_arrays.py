class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        merged = [0]*(m+n)
        i=0
        flag1 = 0
        flag2 = 0
        if m == 0:
            if n % 2 == 1:
                return nums2[len(nums2) // 2]
            else:
                return (float(nums2[n // 2]) + float(nums2[n // 2 - 1])) / 2
        elif n == 0:
            if m % 2 == 1:
                return nums1[m // 2]
            else:
                return (float(nums1[m // 2]) + float(nums1[m // 2 - 1])) / 2
        while len(nums1) >0 and len(nums2) > 0:
            if nums1[0] < nums2[0]:
                merged[i] = nums1[0]
                nums1 = nums1[1:]
                if len(nums1)==0:
                    flag1 = 1
            else:
                merged[i] = nums2[0]
                nums2 = nums2[1:]
                if len(nums2) == 0:
                    flag2 = 1
            i=i+1
        if flag1:
            merged[i:] = nums2
        elif flag2:
            merged[i:] = nums1
        else:
            pass
        if len(merged) % 2 == 1:
            return merged[len(merged) // 2]
        else:
            return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2

s = Solution()
print(s.findMedianSortedArrays([], [1]))