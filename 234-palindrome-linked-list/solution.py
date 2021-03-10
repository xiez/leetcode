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
        
        lst = []
        cur = head
        while mid > 0:
            lst.append(cur.val)            
            cur = cur.next        
            mid -= 1
        print(lst)
        
        if cnt % 2 != 0:
            cur = cur.next
            
        while cur:
            if cur.val == lst[-1]:
                cur = cur.next
                del lst[-1]
            else:
                return False
            
        return True
