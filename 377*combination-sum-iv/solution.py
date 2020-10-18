class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num < 0:
                    continue

                dp[i] += dp[i - num]
        # print(dp)
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum4([1,2,3], 4))
