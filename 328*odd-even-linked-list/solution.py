# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        head_next = head.next

        i = head
        j = head_next
        while i.next and j.next:
            i.next = j.next
            j.next = i.next.next
            
            i = i.next
            j = j.next

        i.next = head_next
        
        return head
