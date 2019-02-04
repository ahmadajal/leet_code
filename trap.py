class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        water = 0
        end = 1
        if len(height) < 3:
            return 0
        while start < len(height) - 1:
            if height[end] >= height[start]:
                water += (height[start] * (end - start - 1)) - sum(height[start + 1:end])
                start = end
                end += 1
            else:
                end += 1
                if end > len(height) - 1:
                    mid = start + 1
                    while mid < end:
                        if height[mid] < height[end - 1]:
                            mid += 1
                        else:
                            water += (height[mid] * (mid - start - 1)) - sum(height[start + 1:mid])
                            start = mid
                            mid += 1
                    break
        print(start, end, mid)
        return water



s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))