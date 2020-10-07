class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        lis = [1] * len(nums)
        cnts = [1] * len(nums)

        for j in range(1, len(nums)):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lis[i] + 1 > lis[j]:
                        lis[j] = lis[i] + 1
                        cnts[j] = cnts[i]
                    elif lis[i] + 1 == lis[j]:
                        cnts[j] += cnts[i]

        max_length = max(lis)
        num_lis = 0
        for idx, e in enumerate(lis):
            if e == max_length:
                num_lis += cnts[idx]
        return num_lis

if __name__ == '__main__':
    s = Solution()

    # print(s.findNumberOfLIS([3,1,2,3,3,4]))

    assert s.findNumberOfLIS([1,1,1,2,2,2,3,3,3]) == 27

    assert s.findNumberOfLIS([10,9,2,5,3,7,101,18]) == 4

    print('Done.')
