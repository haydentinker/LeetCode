# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        def validate(curr, maxVal, minVal):
            if not curr:
                return True
            if curr.val >=maxVal or curr.val <= minVal:
                return False
            return validate(curr.left, curr.val, minVal) and validate(curr.right, maxVal, curr.val)
        return validate(root, float('inf'), float('-inf'))
        
        