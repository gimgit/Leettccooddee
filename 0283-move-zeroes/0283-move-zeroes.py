class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[zero_pointer] == 0:
                nums[zero_pointer], nums[i] = nums[i], nums[zero_pointer]

            if nums[zero_pointer] != 0:
                zero_pointer += 1

