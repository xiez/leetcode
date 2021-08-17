class MyHashMap(object):
    class Entry:
        def __init__(self, key, val, next=None):
            self.key = key
            self.val = val
            self.next = next
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 7919
        self.lst = [None] * self.size 

    def _hash_key(self, key):
        return key % self.size
    
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = self._hash_key(key)
        cur = self.lst[hash_key]
        if cur is None:
            self.lst[hash_key] = self.Entry(key, value)
            return 
        prev = None
        while cur:
            if cur.key == key:
                cur.val = value
                return
            prev = cur
            cur = cur.next
                
        prev.next = self.Entry(key, value)    
            
    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_key = self._hash_key(key)
        cur = self.lst[hash_key]
        if cur is None:
            return -1
        
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hash_key = self._hash_key(key)
        head = self.lst[hash_key]
        if head is None:
            return
        
        prev = None
        while head:
            if head.key == key:
                if prev is None:
                    self.lst[hash_key] = head.next
                else:
                    prev.next = head.next
                return
            else:
                prev = head
                head = head.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
