# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head      

        prev = None
        curr = head
        next = curr.next
        
        while curr:
            curr.next = prev
            
            prev = curr
            curr = next
            if curr:
                next = curr.next
            else:
                next = None
            
        return prev
