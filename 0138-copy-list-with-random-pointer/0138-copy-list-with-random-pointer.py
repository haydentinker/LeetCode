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
        #Create a hash map with None to None
        oldToNew={None:None}
        currNode=head
        #Loop through the list 1 time to initialize copies of nodes
        #We need to do this because some nodes have a random pointer to a future node
        while currNode:
            copyNode=Node(currNode.val)
            oldToNew[currNode]=copyNode
            currNode=currNode.next
        #After initializing nodes, pass through head again and use the hash map to set the next and random pointers
        currNode=head
        while currNode:
            oldToNew[currNode].next=oldToNew[currNode.next]
            oldToNew[currNode].random=oldToNew[currNode.random]
            currNode=currNode.next
        return oldToNew[head]