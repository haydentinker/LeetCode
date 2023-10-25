# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.goodNodesFound=1
    def goodNodes(self, root: TreeNode) -> int:

        self.checkIfGood(root.left,root.val)
        self.checkIfGood(root.right,root.val)
        return self.goodNodesFound
    def checkIfGood(self,root,lastGoodValue):
        if root:
            if root.val>=lastGoodValue:
                lastGoodValue=root.val
                self.goodNodesFound+=1
            self.checkIfGood(root.right,lastGoodValue)
            self.checkIfGood(root.left,lastGoodValue)

    