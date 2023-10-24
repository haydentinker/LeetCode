# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, pRoot: Optional[TreeNode], qRoot: Optional[TreeNode]) -> bool:
       
        if pRoot and qRoot:
            if not (pRoot.val==qRoot.val):
                return False
            left=self.isSameTree(pRoot.left,qRoot.left)
            right=self.isSameTree(pRoot.right,qRoot.right)    
            return left and right
        elif not pRoot and not qRoot:
            return True
        return False
