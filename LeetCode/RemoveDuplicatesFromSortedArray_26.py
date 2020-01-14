class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        i = 1   # 结果数组元素下标指针

        for j in range(1, len(nums)):
            if nums[j - 1] != nums[j]:
                nums[i] = nums[j]
                i += 1

        return i
