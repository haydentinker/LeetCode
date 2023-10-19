# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode()
        resultPointer=result
        list1Node=l1
        list2Node=l2
        carry=0
        print('hi')
        while list1Node and list2Node:
            currentSum=list1Node.val+list2Node.val+carry
            carry=0
    
            if currentSum>=10:
                result.next=ListNode(val=currentSum%10)
                carry=1
            else:
                result.next=ListNode(val=currentSum)
            result=result.next
            list1Node=list1Node.next
            list2Node=list2Node.next
        if list1Node:
            while list1Node:
                currentSum=list1Node.val+carry
                carry=0
                if currentSum>=10:
                    carry=1
                    result.next=ListNode(val=currentSum%10)
                else:
                    result.next=ListNode(val=currentSum)
                result=result.next
                list1Node=list1Node.next
        else:
            while list2Node:
                currentSum=list2Node.val+carry
                carry=0
                if currentSum>=10:
                    carry=1
                    result.next=ListNode(val=currentSum%10)
                else:
                    result.next=ListNode(val=currentSum)
                result=result.next
                list2Node=list2Node.next
        if carry:
            result.next=ListNode(val=1)


        return resultPointer.next