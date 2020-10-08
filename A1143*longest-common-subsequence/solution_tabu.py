class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp_table = [[-1] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        for row in range(len(text2) + 1):
            for col in range(len(text1) + 1):
                if row == 0 or col == 0:
                    dp_table[row][col] = 0
                elif text1[col-1] == text2[row-1]:
                    dp_table[row][col] = 1 + dp_table[row-1][col-1]
                else:
                    dp_table[row][col] = max(dp_table[row][col-1], dp_table[row-1][col])

        return dp_table[len(text2)][len(text1)]

if __name__ == '__main__':
    s = Solution()

    # print(s.longestCommonSubsequence('abc', 'deb'))

    assert s.longestCommonSubsequence('abcde', 'ac') == 2
