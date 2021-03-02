class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1

        try:
            while True:
                while nums[i] == nums[j]:
                    del nums[j]

                i += 1
                j += 1
        except IndexError:
            pass

        return i + 1
