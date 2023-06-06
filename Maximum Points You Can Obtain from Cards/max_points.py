from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = 0
        right_sum = sum(cardPoints[-k:])
        max_value = right_sum
        for i in range(k):
            left_sum += cardPoints[i]
            right_sum -= cardPoints[-(k-i)]
            val = left_sum + right_sum 
            max_value = max(max_value, val)
        return max_value