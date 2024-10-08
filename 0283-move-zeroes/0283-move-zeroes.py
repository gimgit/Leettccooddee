class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_pointer = 0
        for num in range(len(nums)):
            if nums[num] != 0 and nums[zero_pointer] == 0:
                nums[zero_pointer], nums[num] = nums[num], nums[zero_pointer]

            if nums[zero_pointer] != 0:
                zero_pointer += 1




        # # slow = 0
        # for num in range(len(nums)):
        #     if nums[num] != 0 and nums[zero_pointer] == 0:
        #         nums[zero_pointer], nums[num] = nums[num], nums[zero_pointer]

        #     # wait while we find a non-zero element to
        #     # swap with you
        #     if nums[zero_pointer] != 0:
        #         zero_pointer += 1