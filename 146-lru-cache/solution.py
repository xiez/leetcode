class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DLList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.count = 0

    def prepend(self, n):
        old = self.head.next

        self.head.next = n
        n.prev = self.head

        old.prev = n
        n.next = old

        self.count += 1

    def remove(self, n):
        prev = n.prev
        next = n.next

        prev.next = next
        next.prev = prev

        self.count -= 1

    def remove_last(self):
        n = self.tail.prev
        if n.val is not None:
            self.remove(n)

        return n

    def traverse(self):
        p = self.head
        while p.next:
            if p.val is not None:
                print(p.val)
            p = p.next


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.DL_list = DLList()
        self.key_node = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.key_node:
            n = self.key_node[key]
            self.DL_list.remove(n)
            self.DL_list.prepend(n)
            return n.val[1]
        else:
            return -1

    def is_full(self):
        return self.capacity == self.DL_list.count

    def remove_lru_item(self):
        n = self.DL_list.remove_last()
        del self.key_node[n.val[0]]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        n = Node((key, value))

        if self.get(key) == -1:
            if self.is_full():
                self.remove_lru_item()

            self.DL_list.prepend(n)
            self.key_node[key] = n
        else:
            self.key_node[key].val = (key, value)


if __name__ == '__main__':
    # obj = LRUCache(10)
    # param_1 = obj.get(key)
    # obj.put(key,value)

    l = DLList()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    l.prepend(a)
    l.prepend(b)
    l.prepend(c)

    l.traverse()
    print('1--------')

    l.remove(a)
    l.traverse()
    print('2--------')

    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    # c.DL_list.traverse()
    # print(c.get(2))
    assert c.get(2) == -1
    c.put(4, 4)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4

    print('Done')
