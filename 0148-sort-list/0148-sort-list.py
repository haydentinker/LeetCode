# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left=head
        right=self.splitList(head)

        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)
    def merge(self,left,right):
        tail=dummy=ListNode()
        while left and right:
            if left.val <right.val:
                dummy.next=left
                left=left.next
            else:
                dummy.next=right
                right=right.next
            dummy=dummy.next
        if left:
            dummy.next=left
        if right:
            dummy.next=right
        return tail.next
    def splitList(self,root):
        if root and root.next:
            left=root
            right=root.next
            while right and right.next:
                left=left.next
                right=right.next.next
            right=left.next
            left.next=None
            return right
