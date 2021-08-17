"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def _flatten(self, head):
        i = head
        tail = head
        while i:
            if i.child:
                old_head = i
                old_head_next = i.next
                
                new_h, new_t = self._flatten(i.child)
                
                old_head.next = new_h
                new_h.prev = old_head
                
                new_t.next = old_head_next
                if old_head_next:
                    old_head_next.prev = new_t
    
                old_head.child = None
                i = old_head_next
                tail = new_t
            else:
                tail = i
                i = i.next
            
        return head, tail
    
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        new_h, new_t = self._flatten(head)
        return new_h
