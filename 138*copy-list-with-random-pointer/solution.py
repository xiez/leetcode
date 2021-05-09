"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        d = {}
        
        cur = head
        new_head = None
        new_tail = None        

        while cur:
            n = Node(cur.val)
            d[cur] = n

            if new_head is None:
                new_head = n
                new_tail = n                
            else:
                new_tail.next = n
                new_tail = n

            if cur.random is None:
                n.random = None
            else:
                if cur.random in d:
                    #print(f'cur.random in d: {d[cur.random]}')
                    new_tail.random = d[cur.random]
                else:
                    new_tail.random = -1
                    
            cur = cur.next

        cur = head
        cur2 = new_head
        while cur:
            if cur2.random == -1:
                cur2.random = d[cur.random]
                
            cur = cur.next
            cur2 = cur2.next
        
        return new_head
