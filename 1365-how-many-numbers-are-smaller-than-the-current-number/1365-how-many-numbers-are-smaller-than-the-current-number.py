class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        sorted_nums = sorted(nums)
        for num in nums:
            result.append(sorted_nums.index(num))
        return result
            