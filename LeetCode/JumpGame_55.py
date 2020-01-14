class Solution:
    def canJump(self, nums: [int]) -> bool:
        max_index  = 0

        for i in range(0, len(nums)):
            if i > max_index:
                return False
            else:
                max_index = max(i + nums[i], max_index)
            if max_index >= len(nums) - 1:
                return True
        return True
