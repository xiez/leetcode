# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l3 = ListNode()
        tail = l3

        while (l1 is not None and l2 is not None):
            if (l1.val <= l2.val):
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1 is not None:
            tail.next = l1

        if l2 is not None:
            tail.next = l2

        return l3.next

if __name__ == '__main__':
    l1_3 = ListNode(4)
    l1_2 = ListNode(2, next=l1_3)
    l1 = ListNode(1, next=l1_2)

    l2_3 = ListNode(4)
    l2_2 = ListNode(3, next=l2_3)
    l2 = ListNode(1, next=l2_2)

    assert l1.val == 1
    assert l1.next.val == 2
    assert l1.next.next.val == 4

    assert l2.val == 1
    assert l2.next.val == 3
    assert l2.next.next.val == 4

    f = Solution().mergeTwoLists
    l3 = f(l1, l2)

    # print '---------'
    # while l3 is not None:
    #     print l3.val
    #     l3 = l3.next
    # print '---------'

    assert l3.val == 1
    assert l3.next.val == 1
    assert l3.next.next.val == 2
    assert l3.next.next.next.val == 3
    assert l3.next.next.next.next.val == 4
    assert l3.next.next.next.next.next.val == 4
