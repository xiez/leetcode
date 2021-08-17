class Entry {
    int key;
    int val;
    Entry next;
    
    public Entry(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

class MyHashMap {
    Entry[] arr;
    private static int SIZE = 7919;
    /** Initialize your data structure here. */
    public MyHashMap() {
        arr = new Entry[SIZE];
    }

    private int hash_key(int key) {
        return key % SIZE;
    }
    /** value will always be non-negative. */
    public void put(int key, int value) {
        int hkey = hash_key(key);
        Entry cur = arr[hkey];
        if (cur == null) {
            arr[hkey] = new Entry(key, value);
            return;
        }
        
        Entry prev = null;
        while (cur != null) {
            if (cur.key == key) {
                cur.val = value;
                return;
            }
            prev = cur;
            cur = cur.next;
        }
        prev.next = new Entry(key, value);
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        int hkey = hash_key(key);
        Entry cur = arr[hkey];
        if (cur == null) {
            return -1;
        } else{
            while (cur != null) {
                if (cur.key == key) {
                    return cur.val;
                }
                cur = cur.next;
            }
            return -1;
        }
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        int hkey = hash_key(key);
        Entry cur = arr[hkey];
        if (cur == null) {
            return;
        } else {
            Entry prev = null;
            while (cur != null) {
                if (cur.key == key) {
                    if (prev == null) {
                        arr[hkey] = cur.next;
                    } else {
                        prev.next = cur.next;
                    }
                    return;
                } else {
                    prev = cur;
                    cur = cur.next;
                }
            }
        }      
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
