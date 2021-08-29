class Solution(object):
    def __init__(self):
        self.cache = {}
        
    def _countN(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in self.cache:
            return self.cache[n]
        
        if n % 2 == 0:
            ret = self._countN(n / 2)
        else:
            ret = self._countN( n / 2) + 1
        self.cache[n] = ret
        return ret
        
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        for i in range(n+1):
            ret.append(self._countN(i))
            
        return ret
        
        
