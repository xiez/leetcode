class StackOverflowError(Exception):
    pass


class EmptyStackError(Exception):
    pass


class Stack:
    def __init__(self, max_length=100):
        self.lst = []
        self.max_length = max_length

    def is_full(self):
        return len(self.lst) >= self.max_length

    def is_empty(self):
        return len(self.lst) <= 0

    def push(self, n):
        if self.is_full():
            raise StackOverflowError()

        self.lst.append(n)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError()

        return self.lst.pop()

    def top(self):
        if not self.is_empty():
            return self.lst[-1]


class MinStack(Stack):
    def __init__(self, max_length=1000000):
        super().__init__(max_length=max_length)
        self.min_stack = Stack(max_length=max_length)

    def push(self, n):
        super().push(n)

        if self.min_stack.is_empty():
            self.min_stack.push(n)
        else:
            min = self.min_stack.top()
            self.min_stack.push(n) if n <= min else self.min_stack.push(min)

    def pop(self):
        val = super().pop()
        self.min_stack.pop()
        return val

    def getMin(self):
        return self.min_stack.top()

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3

    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2
