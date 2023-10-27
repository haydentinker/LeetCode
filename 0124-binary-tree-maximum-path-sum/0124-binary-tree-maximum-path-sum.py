# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result=float('-inf')
        def sum(root):
            if not root:
                return 0
            right=max(sum(root.right),0)
            left=max (sum(root.left),0)
            current_sum=left+right+root.val
            self.result=max(
                self.result,
                current_sum)
            return root.val+max(left,right)
    
        sum(root)
        return self.result