class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        
        for idx, n in enumerate(nums):
            idx = abs(n) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
            else:
                ret.append(abs(n))
                
        return ret
