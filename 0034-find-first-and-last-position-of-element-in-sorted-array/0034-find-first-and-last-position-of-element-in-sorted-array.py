class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        candidates = []
        for i in range(len(nums)):
            print(nums[i])
            if nums[i] == target:
                candidates.append(i)
        
        if len(candidates):
            return [candidates[0], candidates[-1]]
        return [-1, -1]