# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.res=[]
        self.prev=None
        self.maxCount=0
        self.curCount=0
        self.inorder(root)
      
        return self.res
    def inorder(self,root):
            if not root:
                return
            
            self.inorder(root.left)
            if self.prev is None:
                self.prev=root.val
                self.curCount=1    
            elif self.prev==root.val:
                self.curCount+=1
            else:
                self.prev=root.val
                self.curCount=1

            if self.curCount>self.maxCount:
                self.maxCount=self.curCount
                self.res=[root.val]
            elif self.curCount==self.maxCount:
                self.res.append(root.val)
            
            self.inorder(root.right)

            return