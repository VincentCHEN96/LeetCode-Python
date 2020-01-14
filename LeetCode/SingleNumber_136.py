class Solution:
    def singleNumber(self, nums: [int]) -> int:
        single_number = 0

        for i in range(0, len(nums)):
            single_number ^= nums[i]

        return single_number
