/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function isPalindrome(head: ListNode | null): boolean {
    let slow=head;
    let fast=head;
    while (fast.next?.next){
        slow=slow.next;
        fast=fast.next.next;
    }
    let prev=null;
    let curr=slow.next;
    let nextNode=null
    while(curr){
        nextNode=curr.next;
        curr.next=prev;
        prev=curr;
        curr=nextNode;
    }
    while(head &&prev){
        if (head.val!=prev.val){
            return false;
        }
        head=head.next
        prev=prev.next
    }
    return true;
};