class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1

        while j >= 0:
            n1 = nums1[i]
            n2 = nums2[j]

            if n1 > n2:
                i -= 1
                if i < 0:
                    nums1.insert(0, n2)
                    i = 0
                    j -= 1
            else:
                nums1.insert(i+1, n2)
                j -= 1

            # print(nums1[:m+n])

        nums1[:] = nums1[:m+n]

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    nums2 = [4,5,6]
    Solution().merge(nums1, 3, nums2, 3)

    assert nums1 == [1,2,3,4,5,6]

    nums3 = [4,5,6,0,0,0]
    nums4 = [1,2,3]
    Solution().merge(nums3, 3, nums4, 3)
    assert nums3 == [1,2,3,4,5,6]

    nums5 = [0,0,3,0,0,0,0,0,0]
    nums6 = [-1,1,1,1,2,3]
    Solution().merge(nums5, 3, nums6, 6)
    assert nums5 == [-1,0,0,1,1,1,2,3,3]
