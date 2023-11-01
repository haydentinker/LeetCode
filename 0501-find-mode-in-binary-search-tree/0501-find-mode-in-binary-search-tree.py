# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        tree=[]
        stack=[]
        cur=root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            tree.append(cur.val)
            cur=cur.right
        treeCount=Counter(tree).most_common()
        maxCount=treeCount[0][1]
        return [val for val,count in treeCount if count ==maxCount]