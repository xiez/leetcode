# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        visited = {}
        cur = head
        visited[cur] = cur

        while cur.next is not None:
            if cur.next in visited:
                return True

            visited[cur.next] = cur.next
            cur = cur.next

        return False
