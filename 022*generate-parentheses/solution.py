class Solution:
    def __init__(self):
        self.res = []

    def genParen(self, lst, pos, n, o, c):
        if c == n:
            self.res.append("".join(lst))
        else:
            if o > c:
                lst[pos] = ')'
                self.genParen(lst, pos + 1, n, o, c + 1)
            if o < n:
                lst[pos] = '('
                self.genParen(lst, pos + 1, n, o + 1, c)
    
    def generateParenthesis(self, n: int):
        lst = [""] * 2 * n
        self.genParen(lst, 0, n, 0, 0)
        return self.res
