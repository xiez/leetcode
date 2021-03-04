# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = l1
        j = l2
        prev = None
        plus_one = False

        while i and j:
            iv = i.val
            jv = j.val
            i.val = iv + jv
            if plus_one:
                i.val = i.val + 1

            if i.val >= 10:
                i.val = i.val - 10
                plus_one = True
            else:
                plus_one = False

            j.val = i.val

            prev = i
            i = i.next
            j = j.next

        if i is None and j is None:
            if plus_one:
                prev.next = ListNode(1)
                return l1
            else:
                return l1

        if j:
            prev = None
            while j:
                if plus_one:
                    j.val = j.val + 1
                if j.val == 10:
                    j.val = 0
                    plus_one = True
                else:
                    plus_one = False
                prev = j
                j = j.next
            if plus_one:
                prev.next = ListNode(1)
            return l2

        if i:
            prev = None
            while i:
                if plus_one:
                    i.val = i.val + 1
                if i.val == 10:
                    i.val = 0
                    plus_one = True
                else:
                    plus_one = False
                prev = i
                i = i.next
            if plus_one:
                prev.next = ListNode(1)
            return l1
