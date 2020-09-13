class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            if n in d:
                del d[n]
            else:
                d[n] = 1

        return d.keys()[0]

if __name__ == '__main__':
    s = Solution()

    assert s.singleNumber([2,2,1]) == 1
    assert s.singleNumber([4,1,2,1,2]) == 4

    print('Done!')
