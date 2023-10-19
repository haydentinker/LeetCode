# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Init result LinkedList, dummy pointer, and carry
        result=ListNode()
        resultPointer=result
        carry=0
        while l1 or l2 or carry:
            #Grab list vals else 0
            value1= l1.val if l1 else 0
            value2= l2.val if l2 else 0
            #Add up
            currentSum=value1+value2+carry
            # Set carry and sum
            carry=currentSum // 10
            result.next=ListNode(val=currentSum%10)
            # Update pointers to next
            result=result.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        
        return resultPointer.next