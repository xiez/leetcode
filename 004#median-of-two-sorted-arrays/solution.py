class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i, j = 0, 0

        try:
            while 1:
                a = nums1[i]
                b = nums2[j]
                if a <= b:
                    nums.append(a)
                    i += 1
                else:
                    nums.append(b)
                    j += 1
        except IndexError:
            pass

        if i < len(nums1):
            nums += nums1[i:]

        if j < len(nums2):
            nums += nums2[j:]        

        if len(nums) % 2 == 0:
            i = int(len(nums) / 2)
            return (nums[i] + nums[i-1]) / 2
        else:
            return nums[len(nums) // 2]
