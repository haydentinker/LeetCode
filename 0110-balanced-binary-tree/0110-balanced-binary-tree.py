# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag=True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            self.dfs(root)
        return self.flag

    def dfs(self,root):
        if not root:
            return 0
        if not self.flag:
            return 0
        right=self.dfs(root.right)
        left=self.dfs(root.left)
        if (abs(right-left)>1):
            self.flag=False
        return 1+max(right,left)