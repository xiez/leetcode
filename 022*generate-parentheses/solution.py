import copy

class Solution:
    def __init__(self, ):
        self.ret = ['()']
        
    def generate(self, s):
        ret = []        
        i = 0
        while i <= len(s):
            ret.append(s[:i] + '()' + s[i:])
            i += 1

        return list(set(ret))
    
    def generateParenthesis(self, n: int) -> List[str]:
        i = 1
        while i < n:
            lst = []
            tmp = copy.copy(self.ret)
            for e in tmp:
                ret = self.generate(e)
                for r in ret:
                    if r not in lst:
                        lst.append(r)
            self.ret = lst
            i += 1
            
        return self.ret
