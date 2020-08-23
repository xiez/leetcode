# https://leetcode.com/problems/buddy-strings/

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:              # if two strings are equal
            if len(A) == len(set(A)): # and if all characters are unique
                return False
            else:
                return True

        # two strings are not equal
        if len(A) != len(B): # and if two string lengths differ
            return False

        # two strings are not equal but two string lengths equal
        diff_indexes = []
        for i in range(len(A)):
            if A[i] == B[i]:
                continue
            diff_indexes.append(i)

        if len(diff_indexes) != 2:
            return False

        j, k = diff_indexes
        list_A = list(A)
        list_A[j] = A[k]
        list_A[k] = A[j]
        return ''.join(list_A) == B

if __name__ == '__main__':
    f = Solution().buddyStrings

    print('Start testing...')
    assert f('ab', 'ab') is False
    assert f('abab', 'abab') is True
    assert f('abc', 'abc') is False
    assert f('cabc', 'abcc') is False
    assert f('acabc', 'aabcc') is False
    assert f('ba', 'ab') is True
    assert f('aa', 'aa') is True
    assert f('aba', 'aab') is True
    assert f('baa', 'aab') is True

    print('Done.')
