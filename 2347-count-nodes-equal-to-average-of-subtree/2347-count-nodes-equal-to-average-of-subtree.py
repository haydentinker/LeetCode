# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[0]
        

    def dfs(self,root):
        if not root:
            return None   
        left=self.dfs(root.left)
        right=self.dfs(root.right)
       
        if left==None and right==None:
            return [1,1,root.val]
        elif right==None:
            averageOfSub=(root.val+left[2])//(left[1]+1)
            if root.val==averageOfSub:
                return [left[0]+1,left[1]+1,root.val+left[2]]
            else:
                return [left[0],left[1]+1,root.val+left[2]]
        elif left==None:
            averageOfSub=(root.val+right[2])//(right[1]+1)
            if root.val==averageOfSub:
                print(averageOfSub,root.val)
                return [right[0]+1,right[1]+1,root.val+right[2]]
            else:
                return[right[0],right[1]+1,root.val+right[2]]
        else:
            sumOfSub=root.val+right[2]+left[2]
            averageOfSub=(sumOfSub)//(left[1]+right[1]+1)
            if root.val==averageOfSub:
                return [right[0]+left[0]+1,left[1]+right[1]+1,sumOfSub]
            else:
                return [right[0]+left[0],1+right[1]+left[1],sumOfSub]
