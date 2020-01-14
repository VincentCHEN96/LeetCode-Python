class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        result = []

        if len(nums) < 4:
            return result
        nums.sort()
        for a in range(0, len(nums) - 3):
            if a - 1 >= 0 and nums[a - 1] == nums[a]:
                continue
            for b in range(a + 1, len(nums) - 2):
                if b - 1 >= a + 1 and nums[b - 1] == nums[b]:
                    continue
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if sum < target:
                        c += 1
                    elif sum > target:
                        d -= 1
                    else:
                        result.append([nums[a], nums[b], nums[c], nums[d]])
                        while c + 1 < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d - 1 and nums[d - 1] == nums[d]:
                            d -= 1
                        c += 1
                        d -= 1
        return result
