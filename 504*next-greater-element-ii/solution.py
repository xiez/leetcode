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
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        two_nums = nums + nums
        s = Stack()
        d = {}

        i = 0
        while i < len(two_nums):
            if s.is_empty():
                s.push(i)
                i += 1
                continue

            if two_nums[i] > two_nums[s.top()]:
                while not s.is_empty() and two_nums[i] > two_nums[s.top()]:
                    n = s.pop()  # next greater val of n is nums[i]
                    d[n] = two_nums[i]

                s.push(i)
            else:
                s.push(i)

            i += 1

        while not s.is_empty():
            d[s.pop()] = -1

        ret = []
        i = 0
        while i < len(nums):
            ret.append(d[i])
            i += 1

        return ret
