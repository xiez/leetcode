# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
            
        mid = cnt // 2
        
        prev = None
        curr = head
        next = head.next
        
        while mid > 0:
            curr.next = prev
            
            prev = curr
            curr = next
            next = curr.next
            
            mid -= 1
        
        if cnt % 2 != 0:
            curr = curr.next

        while curr and prev:
            if curr.val != prev.val:
                return False
            
            curr = curr.next
            prev = prev.next
            
        return True
