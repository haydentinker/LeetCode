# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result={}
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.bfs(root,0)
        return list(self.result.values())
    def bfs(self,root,height):
        if root:
            if not height in self.result:
                self.result[height]=root.val
            self.bfs(root.right,height+1)
            self.bfs(root.left,height+1)
            