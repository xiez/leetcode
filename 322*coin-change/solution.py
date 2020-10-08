MAX_INT = 100000000000
NO_COINS = -1

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # fewest number of coins at each amount
        dp_table = [MAX_INT] * (amount + 1)

        dp_table[0] = 0
        for cur_amount in range(1, amount+1):
            for c in coins:
                if cur_amount - c < 0:
                    continue
                elif cur_amount - c == 0:
                    dp_table[cur_amount] = min(
                        dp_table[cur_amount],
                        1
                    )
                else:
                    if dp_table[cur_amount - c] == NO_COINS:
                        continue

                    dp_table[cur_amount] = min(
                        dp_table[cur_amount],
                        1 + dp_table[cur_amount - c],
                    )

            if dp_table[cur_amount] == MAX_INT:
                dp_table[cur_amount] = NO_COINS

        return dp_table[amount]

if __name__ == '__main__':
    s = Solution()

    assert s.coinChange([2,], 3) == -1

    # assert s.coinChange([1,2,5,], 11) == 3

    assert s.coinChange([186,419,83,408], 6249) == 20
