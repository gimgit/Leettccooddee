# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node, num):
            if node:
                if node.left == None and node.right == None:
                    num += str(node.val)
                    self.res += int(num, 2)
                dfs(node.left, num+str(node.val))
                dfs(node.right, num+str(node.val))

        dfs(root, "")

        return self.res