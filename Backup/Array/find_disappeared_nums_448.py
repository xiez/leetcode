class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            val = abs(nums[i])

            idx = val -1
            nums[idx] = -1 * abs(nums[idx])

        ret = []
        n = 0
        while n < len(nums):
            if nums[n] < 0:
                n += 1
                continue

            ret.append(n+1)
            n += 1

        return ret

if __name__ == '__main__':
    f = Solution().findDisappearedNumbers

    input = [4,3,2,7,8,2,3,1]
    output = [5,6]

    assert f(input) == output
