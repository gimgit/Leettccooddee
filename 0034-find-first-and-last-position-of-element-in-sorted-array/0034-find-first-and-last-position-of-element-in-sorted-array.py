class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.binary(nums, target, True)
        end = self.binary(nums, target, False)
        return [start, end]

    def binary(self, nums, target, is_start):
        s = 0
        e = len(nums) - 1
        ans = -1
        while s <= e:
            mid = (s + e) // 2
            if target > nums[mid]:
                s = mid + 1
            elif target < nums[mid]:
                e = mid - 1
            else:
                ans = mid
                if is_start:
                    e = mid - 1
                else:
                    s = mid + 1
        return ans