class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                temp_target = target - nums[i]
                if temp_target == nums[j]:
                    return [i, j]

        return []   #找不到则返回空列表
