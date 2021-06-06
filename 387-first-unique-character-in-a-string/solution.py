class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
              
        for idx, ch in enumerate(s):
            if d[ch] == 1:
                return idx
            
        return -1
