from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        elif m == 0:
            nums1[:] = nums2[:]
            return
        else:
            ind1, ind2 = 0, 0
            while ind1 < m+ind2 and ind2 < n:
                if nums1[ind1] <= nums2[ind2]:
                    ind1 = ind1+1
                else:
                    nums1[:] = nums1[:ind1] + [nums2[ind2]] + nums1[ind1:]
                    nums1[:] = nums1[:-1]
                    ind2 = ind2+1
                    ind1 = ind1+1
            nums1[m+ind2:] = nums2[ind2:]
            print(nums1)
            return