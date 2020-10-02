class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.slots = [-1] * self.size
        

    def _resize(self, new_size):
        new_slots = [-1] * new_size
        idx = 0
        for ele in self.slots:
            new_slots[idx] = ele
            idx += 1

        self.slots = new_slots

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        if (key > self.size -1):
            self._resize(new_size=key)

        self.slots[key] = value
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        try:
            return self.slots[key]
        except IndexError:
            return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        try:
            self.slots[key] = -1
        except IndexError:
            pass
        

if __name__ == '__main__':
    print 'start test'


    hashMap = MyHashMap()
    hashMap.put(1, 1);          
    hashMap.put(2, 2);         
    print hashMap.get(1);
    print hashMap.get(3); 
    print hashMap.put(2, 1);
    print hashMap.get(2);    
    hashMap.remove(2);  
    print hashMap.get(2);      
    

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
