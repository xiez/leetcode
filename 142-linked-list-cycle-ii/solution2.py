# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow_p = head
        fast_p = head

        meet_p = None
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                meet_p = slow_p
                break

        if meet_p is None:
            return None

        slow_p = head
        while slow_p != fast_p:
            slow_p = slow_p.next
            fast_p = fast_p.next

        return slow_p
