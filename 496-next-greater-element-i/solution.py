class Stack:
    def __init__(self):
        self.lst = []

    def push(self, n):
        self.lst.append(n)

    def pop(self):
        return self.lst.pop()

    def top(self):
        return self.lst[-1]

    def is_empty(self):
        return len(self.lst) == 0

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = Stack()
        d = {}

        for e in nums2:
            if s.is_empty():
                s.push(e)
                continue

            if e > s.top():
                while not s.is_empty() and e > s.top():
                    e1 = s.pop()
                    # next greater element of e1 is e
                    d[e1] = e

                s.push(e)
            else:
                s.push(e)

        while not s.is_empty():
            d[s.pop()] = -1

        ret = []
        for e in nums1:
            ret.append(d[e])

        return ret
