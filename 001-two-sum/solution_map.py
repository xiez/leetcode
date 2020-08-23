class Solution:
    def twoSum(self, nums, target):
        d = {}
        for idx, n in enumerate(nums):
            if n in d:
                val = d[n]
                if isinstance(val, list):
                    d[n].append(idx)
                else:
                    d[n] = [val, idx]
            else:
                d[n] = idx

        for idx, n in enumerate(nums):
            if target - n not in d:
                continue

            val = d[target - n]
            if isinstance(val, list):
                for ele in val:
                    if ele == idx:
                        continue
                    return [idx, ele]

            if val == idx:
                continue

            return [idx, val]

if __name__ == '__main__':
    f = Solution().twoSum

    assert f([2, 7, 11, 15], 9) == [0, 1]
    assert f([2, 11, 7, 15], 9) == [0, 2]
    assert f([3, 2, 4], 6) == [1, 2]
    assert f([3, 3], 6) == [0, 1]
