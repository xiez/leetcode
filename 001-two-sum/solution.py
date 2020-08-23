class Solution:
    def twoSum(self, nums, target):
        i, j = 0, 1

        while True:
            try:
                a = nums[i]
            except IndexError:
                break

            try:
                b = nums[j]
            except IndexError:
                i = i + 1
                j = i + 1
                continue

            if a + b == target:
                return [i, j]
            else:
                j = j + 1


if __name__ == '__main__':
    f = Solution().twoSum

    assert f([2, 7, 11, 15], 9) == [0, 1]
    assert f([2, 11, 7, 15], 9) == [0, 2]
