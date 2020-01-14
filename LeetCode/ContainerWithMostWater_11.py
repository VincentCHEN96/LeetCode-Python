class Solution:
    def maxArea(self, height: [int]) -> int:
        max_capacity = 0
        round = 1
        start = 0
        end = len(height) - 1   # slip window

        while end >= 0:
            while end < len(height):
                max_capacity = max((end - start) * min(height[start], height[end]), max_capacity)
                start += 1
                end += 1
            round += 1
            start = 0
            end = len(height) - round

        return max_capacity
