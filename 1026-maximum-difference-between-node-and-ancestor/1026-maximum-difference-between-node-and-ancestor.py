# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root,currMin,currMax):
            if not root:
                return 0
            result=max(abs(root.val-currMin),abs(root.val-currMax)
            )
            newMax=max(root.val,currMax) 
            newMin=min(currMin,root.val)
            return max(result,dfs(root.left,newMin,newMax),dfs(root.right,newMin,newMax))   
        
        return dfs(root,root.val,root.val)


        