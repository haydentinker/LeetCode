# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjacent=defaultdict(list)
        visited=set()
        def buildList(root):
            if not root:
                return
            buildList(root.left)
            buildList(root.right)
            if root.left:
                adjacent[root.val].append(root.left.val)
                adjacent[root.left.val].append(root.val)
            if root.right:
                adjacent[root.val].append(root.right.val)
                adjacent[root.right.val].append(root.val)
            return
        

        buildList(root)
        result=-1
        queue=[start]
        visited=set()
        visited.add(start)
        
        while queue:
            for _ in range(len(queue)):
                val=queue.pop(0)
                for i in adjacent[val]:
                    if i not in visited:
                        queue.append(i)
                        visited.add(i)
            result+=1
        return result
            

        