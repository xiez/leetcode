class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue

                dp[i] = min(dp[i], dp[i - coin] + 1)

        # print(dp)
        return -1 if dp[amount] == float('inf') else dp[amount]


if __name__ == '__main__':
    s = Solution()

    # assert s.coinChange([2,], 3) == -1

    assert s.coinChange([1,2,5,], 11) == 3

    # assert s.coinChange([186,419,83,408], 6249) == 20
