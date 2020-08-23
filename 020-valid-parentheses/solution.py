class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []

        for c in s:
            if len(l) == 0:
                if c in [')', '}', ']']:
                    return False
                else:
                    l.append(c)
            else:
                if c in ['(', '{', '[']:
                    l.append(c)
                else:
                    last = l[-1]
                    if c == '}' and last == '{':
                        l.pop()
                        continue
                    if c == ')' and last == '(':
                        l.pop()
                        continue
                    if c == ']' and last == '[':
                        l.pop()
                        continue

                    return False

        return True if len(l) == 0 else False

if __name__ == '__main__':
    f = Solution().isValid

    assert f('()') is True
    assert f('()[]{}') is True
    assert f('([)]') is False
