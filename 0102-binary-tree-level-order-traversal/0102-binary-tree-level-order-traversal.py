# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result={}
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.appendChildren(root,0)
        return list(self.result.values())
    def appendChildren(self,root,height):
        if root:
            if height not in self.result:
                self.result[height]=[]
            self.result[height].append(root.val)
            self.appendChildren(root.left,height+1)
            self.appendChildren(root.right,height+1)
        
