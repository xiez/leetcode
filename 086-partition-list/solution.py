# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.tail = None
        self.cnt = 0
        
    def move_to_end(self, cur):       
        self.tail.next = cur
        cur.next = None
        self.tail = cur
        
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or head.next is None:
            return head
        
        cur = head
        while cur:
            self.cnt += 1
            self.tail = cur
            cur = cur.next
        
        cur = head
        prev = None
        new_head = head
        #print(self.cnt)
        while self.cnt > 0:
            #print(cur)
            if cur.val >= x:
                if cur is new_head:
                    new_head = new_head.next
                    prev = None
                    cur_copy = cur
                    self.move_to_end(cur_copy)
                    cur = new_head
                elif cur is self.tail:
                    pass
                else:
                    prev.next = cur.next
                    cur_copy = cur                                        
                    cur = cur.next
                    self.move_to_end(cur_copy)
            else:
                prev = cur
                cur = cur.next            
                
            self.cnt -= 1
        
        return new_head
