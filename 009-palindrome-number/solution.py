class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        if x == 0:
            return True

        tmp_x = x
        new_x = 0
        while tmp_x != 0:
            r = tmp_x % 10
            tmp_x = tmp_x / 10
            new_x = new_x * 10 + r

        return x == new_x

if __name__ == '__main__':
    f = Solution().isPalindrome

    assert f(12345) is False
    assert f(121) is True
    assert f(-121) is False
    assert f(10) is False

    print('Done.')
