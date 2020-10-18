class Solution(object):
    def __init__(self):
        self.d = {}

    def _key(self, amount, end):
        return '%s-%s' % (amount, end)

    def _change(self, amount, coins, end):
        if amount == 0:
            return 1
        elif amount < 0:
            return 0
        elif end < 0:
            return 0

        key = self._key(amount, end)
        if key in self.d:
            return self.d[key]

        r1 = self._change(amount, coins, end - 1)
        r2 = self._change(amount - coins[end], coins, end)

        self.d[key] = r1 + r2
        # print(key)
        return r1 + r2

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        return self._change(amount, coins, len(coins) - 1)

if __name__ == '__main__':
    s = Solution()

    # print(s.change(100, [1, 5, 10, 25]))
