class Solution(object):
    def _search(self, nums, target, low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            return self._search(nums, target, mid+1, high)

        else:
            return self._search(nums, target, low, mid-1)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        return self._search(nums, target, low, high)


if __name__ == '__main__':
    f = Solution().search

    assert f([-1,0,3,5,9,12], 9) == 4
    assert f([-1,0,3,5,9,12], 2) == -1

    print('Done!')
