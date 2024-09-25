# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = rec(nums[:mid])
            node.right = rec(nums[mid + 1:])
            return node

        return rec(nums)