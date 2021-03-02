class Stack:
    def __init__(self):
        self.lst = []

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def peek(self):
        return self.lst[-1]

    def empty(self):
        return len(self.lst) == 0

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s2.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.s1.empty():
            while not self.s2.empty():
                self.s1.push(self.s2.pop())

        return self.s1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """

        if self.s1.empty():
            while not self.s2.empty():
                self.s1.push(self.s2.pop())

        return self.s1.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.s1.empty() and self.s2.empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
