# O(n^2)
class Solution(object):
    def __init__(self):
        self.d = {}
        self.max_length = 1

    def _lengthOfLISAtN(self, nums, n):
        if n == 0:
            return 1

        if n in self.d:
            return self.d[n]

        max_length_at_n = 1
        for i in range(n):
            if nums[i] < nums[n]:
                tmp = self._lengthOfLISAtN(nums, i)
                if tmp + 1 > max_length_at_n:
                    max_length_at_n += 1

        if max_length_at_n > self.max_length:
            self.max_length = max_length_at_n

        self.d[n] = max_length_at_n

        return max_length_at_n

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        for n in range(len(nums)):
            a = self._lengthOfLISAtN(nums, n)
            # print('max length at %d is %d' % (n, a))

        return self.max_length

if __name__ == '__main__':
    s = Solution()

    # print(s.lengthOfLIS([1,2,3,1]))

    # assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4

    print('Done.')
