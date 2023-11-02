"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    
        nodeMap={}
        def createClone(oldNode):
            if oldNode:
                newNode=Node(oldNode.val)
                nodeMap[oldNode.val]=newNode
                neighbors=[]
                for i in oldNode.neighbors:
                    if i.val not in nodeMap:
                        neighborClone=createClone(i)
                        
                    else:
                        neighborClone=nodeMap[i.val]    
                    neighbors.append(neighborClone)
                if neighbors:
                    newNode.neighbors=neighbors

                return newNode
        
        print(nodeMap)
        return createClone(node)