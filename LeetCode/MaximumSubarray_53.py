class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        if not nums:
            return 0
        max_sum = -(2 ** 31)
        slip_window_size = 1
        start = end = 0
        while end < len(nums):
            while end < len(nums):
                temp_sum = 0
                while start <= end:
                    temp_sum += nums[start]
                    start += 1
                if temp_sum > max_sum:
                    max_sum = temp_sum
                end += 1
                start = end - slip_window_size + 1
            start = 0
            end = slip_window_size
            slip_window_size += 1

        return max_sum
