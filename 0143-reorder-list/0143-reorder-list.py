# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Get the second half
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        secondHalf=slow.next
        prevNode=slow.next=None
        #Reverse it
        while secondHalf:
            nextNode=secondHalf.next
            secondHalf.next=prevNode
            prevNode=secondHalf
            secondHalf=nextNode
        #Reorder LinkedList
        secondHalf=prevNode
        firstHalf=head
        while secondHalf:
            temp1,temp2=firstHalf.next,secondHalf.next
            firstHalf.next=secondHalf
            secondHalf.next=temp1
            firstHalf,secondHalf=temp1,temp2



            
        