class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) <= len(nums2):
            small = nums1
            large = nums2
        else:
            small = nums2
            large = nums1
            
        d = {}
        for e in large:
            if e in d:
                d[e] += 1
            else:
                d[e] = 1
                
        ret = []
        for n in small:
            if n in d and d[n] > 0:
                ret.append(n) 
                d[n] -= 1
            
        return ret
                
