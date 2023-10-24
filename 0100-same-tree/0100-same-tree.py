# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def compareTrees(pRoot,qRoot):
        
            if pRoot and qRoot:
                if not (pRoot.val==qRoot.val):
                    return False
                left=compareTrees(pRoot.left,qRoot.left)
                right=compareTrees(pRoot.right,qRoot.right)    
                return left and right
            elif not pRoot and not qRoot:
                return True
            return False

        return compareTrees(p,q)