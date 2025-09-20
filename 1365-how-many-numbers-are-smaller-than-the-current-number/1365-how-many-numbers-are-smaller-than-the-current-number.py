class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        d = {}
        ans = []
        for i in range(len(temp)):
            if temp[i] not in d:
                d[temp[i]] =  i
        for i in range(len(temp)):
            ans.append(d[nums[i]])
        return ans

