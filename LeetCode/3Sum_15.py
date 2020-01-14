class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        result = []

        if len(nums) < 3:
            return result
        nums.sort()
        for low in range(0, len(nums) - 2):
            if nums[low] > 0:
                break
            if (low - 1 >= 0) and nums[low - 1] == nums[low]:
                continue
            mid = low + 1
            high = len(nums) - 1
            while mid < high:
                sum = nums[low] + nums[mid] + nums[high]
                if sum < 0:
                    mid += 1
                elif sum > 0:
                    high -= 1
                else:
                    result.append([nums[low], nums[mid], nums[high]])
                    while mid + 1 <= high and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid <= high - 1 and nums[high - 1] == nums[high]:
                        high -= 1
                    mid += 1
                    high -= 1
        return result
