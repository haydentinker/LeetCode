"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew={None:None}
        currNode=head
        while currNode:
            copyNode=Node(currNode.val)
            oldToNew[currNode]=copyNode
            currNode=currNode.next
        currNode=head
        while currNode:
            oldToNew[currNode].next=oldToNew[currNode.next]
            oldToNew[currNode].random=oldToNew[currNode.random]
            currNode=currNode.next
        return oldToNew[head]