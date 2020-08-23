class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        arr = []
        for l in str:
            ord_l = ord(l)
            if ord_l > 64 and ord_l < 91:
                arr.append(chr(ord_l + 32))
            else:
                arr.append(l)
        return ''.join(arr)

if __name__ == '__main__':
    print Solution().toLowerCase('Hello')
