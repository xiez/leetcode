import random

DEBUG = False

def log(msg):
    if DEBUG:
        print(msg)

class Solution:
    def swap(self, nums, i, j):
        if i == j:
            return

        nums[i], nums[j] = nums[j], nums[i]

    def pivot_idx(self, nums, low, high, mid):
        return high

        # TODO: random pivot choice
        # idx = random.randint(low, high)
        # return (idx, nums[idx])

        # # median of three
        # l, m, h = nums[low], nums[mid], nums[high]

        # if (l <= m and l >= h) or (l <= h and l >= m):
        #     return low

        # if (m <= l and m >= h) or (m <= h and m >= l):
        #     return mid

        # if (h <= l and h >= m) or (h <= m and h >= l):
        #     return high

        # assert False, 'Should not reach here'

    def partition(self, nums, low, high):
        # partition to (large -> pivot -> small)
        if low == high:
            return low

        assert low < high

        pivot_idx = self.pivot_idx(nums, low, high, (low + high) // 2)
        pivot = nums[pivot_idx]
        log(f'pivot_idx: {pivot_idx}, pivot: {pivot}')
        i, j = low - 1, low

        while j < high:
            if nums[j] >= pivot:
                i += 1
                self.swap(nums, i, j)

            j += 1

        self.swap(nums, i + 1, pivot_idx)
        return i + 1

    def quickselect(self, nums, low, high, k):
        i = self.partition(nums, low, high)
        log(f'partition: {i}')
        log(f'nums after partition: {nums}')

        if i == k - 1:
            log(f'found at index{i}, and num: {nums[i]}')
            return nums[i]
        elif i < k - 1:
            # find in the right(small) part
            return self.quickselect(nums, i + 1, high, k)
        else:
            # find in the left(large) part
            return self.quickselect(nums, low, i - 1, k)

    def findKthLargest(self, nums, k) -> int:
        low = 0
        high = len(nums) - 1

        return self.quickselect(nums, low, high, k)


if __name__ == '__main__':
    s = Solution()

    arr = [3,2,1,5,6,4]
    print(arr)
    assert s.findKthLargest(arr, 2) == 5

    arr = [3,2,3,1,2,4,5,5,6]
    print(arr)
    assert s.findKthLargest(arr, 4) == 4
