# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        listOfElements=[]
        def appendVal(root,elementList):
            if not root:
                return
            elementList.append(root.val)
            appendVal(root.left,elementList)
            appendVal(root.right,elementList)

        appendVal(root,listOfElements)

        
        return sorted(listOfElements)[k-1]
        