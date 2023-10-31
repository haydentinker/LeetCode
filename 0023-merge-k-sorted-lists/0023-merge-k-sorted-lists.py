# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root=ListNode()
        currNode=root
        while lists:
            min=float('inf')
            minIndex=-1
            for i in range(len(lists)):
                if lists[i] and lists[i].val<min:
                    min=lists[i].val
                    minIndex=i
                
        
            if not lists[minIndex]: 
                break
            newNode=ListNode(lists[minIndex].val)
            if lists[minIndex].next==None:
                del lists[minIndex]
            else:
                lists[minIndex]=lists[minIndex].next
            currNode.next=newNode
            currNode=currNode.next
    
            

        return root.next