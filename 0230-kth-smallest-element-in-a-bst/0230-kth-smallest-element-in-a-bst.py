# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        def traverse(curr):
            if not curr or len(nodes) >=k:
                return 
            if curr.left:
                traverse(curr.left)
            nodes.append(curr.val)
            if curr.right:
                traverse(curr.right)
        traverse(root)
        return nodes[k-1]
        
            