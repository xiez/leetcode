NO_COINS = float('inf')

class Solution(object):
    def __init__(self):
        self.dp = {}

    def _coinChange(self, coins, amount):
        if amount == 0:
            return 0

        key = '%s-%s' % (coins, amount)
        if key in self.dp:
            # print(key,self.dp[key])
            return self.dp[key]

        res = []
        for coin in coins:
            if coin > amount:
                continue

            res.append(1 + self._coinChange(coins, amount - coin))

        if not res:
            ret = NO_COINS
        else:
            ret = min(res)

        self.dp[key] = ret
        return ret

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ret = self._coinChange(coins, amount)
        return -1 if ret == NO_COINS else ret

if __name__ == '__main__':
    s = Solution()

    # print(s.coinChange([2], 3))
    # assert s.coinChange([2], 3) == -1

    # assert s.coinChange([1,2,5,], 11) == 3

    # print(s.coinChange([186,419,83,408], 6249))
    # assert s.coinChange([186,419,83,408], 6249) == 20

    print('Done.')
