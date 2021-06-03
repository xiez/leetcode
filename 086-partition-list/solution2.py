# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l1 = ListNode() # < x
        l2 = ListNode() # >= x
        l1_tail = l1
        l2_tail = l2
        
        cur = head
        while cur:
            cur_next = cur.next
            if cur.val < x:
                if l1_tail is l1:
                    l1.next = cur
                else:
                    l1_tail.next = cur
                
                l1_tail = cur
                cur.next = None
            else:
                if l2_tail is l2:
                    l2.next = cur
                else:
                    l2_tail.next = cur

                l2_tail = cur
                cur.next = None
                
            cur = cur_next            

        l1_tail.next = l2.next
        l2_tail.next = None
        
        return l1.next
