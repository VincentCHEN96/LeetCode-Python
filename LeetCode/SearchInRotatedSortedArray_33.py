class Solution:
    def search(self, nums: [int], target: int) -> int:
        rotate_index = self.search_rotate_index(nums)

        if rotate_index == -1:
            return -1
        elif rotate_index - 1 >= 0 and nums[0] <= target and target <= nums[rotate_index - 1]:
            return self.binary_search(nums, 0, rotate_index - 1, target)
        else:
            return self.binary_search(nums, rotate_index, len(nums) - 1, target)

    def search_rotate_index(self, nums: [int]) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = int((low + high) / 2)
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return mid + 1
            elif nums[low] <= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return 0 if len(nums) > 0 else -1

    def binary_search(self, nums: [int], low: int, high: int, target: int) -> int:
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] < target:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid
        return -1
