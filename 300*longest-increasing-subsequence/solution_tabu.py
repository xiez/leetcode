class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        lis = [1] * len(nums)

        for j in range(1, len(nums)):
            for i in range(j):
                if nums[j] > nums[i] and lis[i] + 1 > lis[j]:
                    lis[j] = lis[i] + 1

            # print("j: %d, lis: %s" % (nums[j], lis))

        return max(lis)

if __name__ == '__main__':
    s = Solution()

    assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    print('Done.')
