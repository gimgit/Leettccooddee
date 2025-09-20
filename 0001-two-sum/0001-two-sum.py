class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j in range(0, len(nums) - 1):
            for i in range(1, len(nums)):
                if i != j and nums[j] + nums[i] == target:
                    return [j, i]
