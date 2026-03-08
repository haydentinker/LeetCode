# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.calculateDepth(root)

    def calculateDepth(self, root) -> int:
        if(not root):
            return 0 
        rightRes = self.calculateDepth(root.right)
        leftRes = self.calculateDepth(root.left)
        if rightRes == 0:
            return 1+leftRes
        if leftRes == 0:
            return 1+rightRes
        return 1 + min(leftRes, rightRes)
