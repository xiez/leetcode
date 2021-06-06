class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0 or k == len(nums):
            return
        
        if k > len(nums):
            k = k % len(nums)
            
        tmp = nums[-k:]

        i = len(nums) - k - 1
        while i >= 0:
            nums[i+k] = nums[i]
            i -= 1
                    
        i = 0
        while i < len(tmp):
            nums[i] = tmp[i]
            i += 1
