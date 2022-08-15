class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        for i in range(1, n):
            if i == 1:
                left_max[i] = height[i - 1]
            else:
                left_max[i] = max(left_max[i - 1], height[i - 1])
        for i in reversed(range(n - 1)):
            if i == n - 2:
                right_max[i] = height[i + 1]
            else:
                right_max[i] = max(right_max[i + 1], height[i + 1])
        total = 0
        for ind, e in enumerate(height):
            total += max((min(left_max[ind], right_max[ind]) - e), 0)
        return total

