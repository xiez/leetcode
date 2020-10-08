class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # print(text1,text2)
        if len(text1) == 0 or len(text2) == 0:
            return 0

        if text1[-1] == text2[-1]:
            return self.longestCommonSubsequence(text1[:-1], text2[:-1]) + 1
        else:
            return max(
                self.longestCommonSubsequence(text1[:-1], text2),
                self.longestCommonSubsequence(text1, text2[:-1]),
            )

if __name__ == '__main__':
    s = Solution()

    # print(s.longestCommonSubsequence('abc', 'deb'))

    assert s.longestCommonSubsequence('abcde', 'ace') == 3
