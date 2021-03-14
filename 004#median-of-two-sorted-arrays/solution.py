class Solution:
    def meet_cond(self, A, l, h, B, l2, h2):
        try:
            if l2 == -1 and h2 == -1:
                return True if A[h] <= B[0] else False
            else:
                return True if A[h] <= B[h2+1] and B[h2] <= A[h+1] else False
        except IndexError:
                return True

    def have_median(self, A, la, ha, B, lb, hb):
        assert la >= 0 and ha >= 0 and ha <= len(A)
        #assert lb >= 0 and hb >= 0 and hb <= len(B)
        
        if hb == -1:
            # B contributes no elems
            return True

        hb_1 = False if hb+1 >= len(B) else True
        ha_1 = False if ha+1 >= len(A) else True
            
        if A[ha] >= B[hb]:
            if hb_1:
                return True if A[ha] <= B[hb+1] else False
            else:
                return True

        if B[hb] >= A[ha]:
            if ha_1:
                return True if B[hb] <= A[ha+1] else False
            else:
                return True

    def max_two_median(self, t):
        a, b = sorted(t, reverse=True)[:2]
        return (a + b) / 2
    
    def get_median(self, A, la, ha, B, lb, hb):
        len_A, len_B = len(A), len(B)
        is_even = True if (len_A+len_B) % 2 == 0 else False
        
        if hb == -1:
            # B contribs no eles
            if is_even:
                return (A[ha] + A[ha-1]) / 2
            else:
                return A[ha]
            
        if is_even:
            t = (A[ha], B[hb])
            if ha > 0:
                t += (A[ha-1],)
            if hb > 0:
                t += (B[hb-1],)
            return self.max_two_median(t)
        else:
            return A[ha] if A[ha] >= B[hb] else B[hb]
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m >= n:
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
            
        len_A, len_B = len(A), len(B)
        #print(f'lenA:{len_A}, lenB:{len_B}')
        if len_B == 0:
            if len_A % 2 == 0:
                mid = int(len_A / 2)
                return (A[mid] + A[mid-1]) /2
            else:
                mid = len_A // 2
                return A[mid]
   
        contrib_range = int((m + n) / 2) + 1 if (m + n) % 2 == 0 else (m + n) // 2 + 1
        for a_contrib in range(1, contrib_range + 1):
            b_contrib = contrib_range - a_contrib
            if b_contrib > len_B:
                continue
                
            print(f'a contrib:{a_contrib}, b contrib: {b_contrib}')
            if self.have_median(A, 0, a_contrib-1, B, 0, b_contrib - 1):
                print(f'meet cond: A:[0, {a_contrib-1}], B:[0, {b_contrib-1}]')
                return self.get_median(A, 0, a_contrib-1, B, 0, b_contrib-1)
            
        assert False
        # A contributes [1,m] nums, use bin-search to find the exact nums A contributes
                
        
        l_A = 0
        h_A = m - 1
        m_A = (m - 1) / 2
        
        # A - [0, m-1], B - [-1, -1], meet condition ?
        if m == n:
            b_l, b_h = 0, 0
        else:
            b_l, b_h = -1, -1
            
        a_l, a_h = 0, min((len(A)+len(B)) // 2, len(A) - 1)

        i = 100
        while i > 0:
            if self.meet_cond(A, a_l, a_h, B, b_l, b_h):
                print(f'meet cond: A[{a_l}, {a_h}], B[{b_l}, {b_h}]')
                if (m + n) % 2 == 0:
                    if b_h == -1:
                        return (A[a_h-1] + A[a_h]) / 2
                    
                    b_h_1 = b_h - 1 if b_h - 1 >= 0 else 0
                    a_h_1 = a_h - 1 if a_h -1 >= 0 else 0
                    
                    if A[a_h] >= B[b_h_1] and B[b_h] >= A[a_h_1]:
                        return (A[a_h] + B[b_h]) / 2
                    elif A[a_h_1] >= B[b_h]:
                        return (A[a_h_1] + A[a_h]) / 2
                    else:
                        return (B[b_h_1] + B[b_h]) / 2
                else:
                    if b_h == -1:
                        return (A[a_h-1] + A[a_h]) / 2
                    
                    if A[a_h-1] <= B[b_h] and A[a_h] >= B[b_h]:
                        return A[a_h] if A[a_h] >= B[b_h] else B[b_h]
                    else:
                        return (A[a_h-1] + A[a_h]) / 2
            else:
                print(f'NOT meet cond: A({a_l}, {a_h}), B({b_l}, {b_h})')

            a_h -= 1
            if b_l == -1:
                b_l, b_h = 0, 0
            else:
                b_h += 1

            i -= 1
        assert False
        return None
            
        
