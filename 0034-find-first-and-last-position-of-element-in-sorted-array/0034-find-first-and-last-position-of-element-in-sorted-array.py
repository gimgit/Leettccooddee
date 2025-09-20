class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        candidates = []
        if nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    candidates.append(i)
        if candidates:
            return [min(candidates), max(candidates)]
        else:
            return [-1, -1]
