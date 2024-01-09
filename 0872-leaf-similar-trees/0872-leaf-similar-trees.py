# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(root,leaves):
            if not root:
                return None
            left=dfs(root.left,leaves)
            right=dfs(root.right,leaves)
            if left is None and right is None:
                leaves.append(root.val)
            return root.val
        leaves1=[]
        leaves2=[]
        dfs(root1,leaves1)
        dfs(root2,leaves2)
        return leaves1==leaves2
                
            