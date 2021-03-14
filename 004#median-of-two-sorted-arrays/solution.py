import math

class Solution:
    def meet_median_cond(self, A, la, ha, B, lb, hb):
        """Check whether current range of two arrays meet median condition."""
        assert la >= 0 and ha >= 0 and ha <= len(A)

        if hb == -1:
            # B contributes no elems
            return True, False

        hb_1 = False if hb+1 >= len(B) else True
        ha_1 = False if ha+1 >= len(A) else True

        if A[ha] >= B[hb]:
            if hb_1:
                return (True, False) if A[ha] <= B[hb+1] else (False, False)
            else:
                return True, False

        if B[hb] >= A[ha]:
            if ha_1:
                return (True, False) if B[hb] <= A[ha+1] else (False, True)
            else:
                return True, False

    def get_median(self, A, la, ha, B, lb, hb):
        """Get median of two arrays."""
        len_A, len_B = len(A), len(B)
        is_even = True if (len_A + len_B) % 2 == 0 else False

        if hb == -1:
            # B contribs no elems
            assert ha - 1 >= 0
            return (A[ha] + A[ha - 1]) / 2 if is_even else A[ha]

        if is_even:
            t = (A[ha], B[hb])
            if ha > 0:
                t += (A[ha-1],)
            if hb > 0:
                t += (B[hb-1],)

            return sum(sorted(t, reverse=True)[:2]) / 2
        else:
            return A[ha] if A[ha] >= B[hb] else B[hb]

    def get_array_median(self, A, len_A):
        """Get sorted array median."""
        if len_A % 2 == 0:
            mid = int(len_A / 2)
            return (A[mid] + A[mid-1]) / 2
        else:
            mid = len_A // 2
            return A[mid]

    def next_contrib_n(self, max_contrib_n, starts=1):
        i = starts
        while i <= max_contrib_n:
            yield i
            i += 1

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        A, B = (nums1, nums2) if m >= n else (nums2, nums1)

        len_A, len_B = len(A), len(B)
        if len_B == 0:
            # Edge case: one array is empty.
            return self.get_array_median(A, len_A)

        # A contributes at least one elements, at most all elements to the final half array
        # If the length of two arrays is odd, the length of final array is floor(L / 2) + 1
        # else, the length is L / 2 + 1. (L = m + n)
        contrib_n = math.floor((m + n) / 2) + 1

        # for a_contrib in self.next_contrib_n(contrib_n):
        #     b_contrib = contrib_n - a_contrib
        #     if b_contrib > len_B:
        #         continue

        #     print(f'a contrib:{a_contrib}, b contrib: {b_contrib}')
        #     if self.meet_median_cond(A, 0, a_contrib - 1, B, 0, b_contrib - 1):
        #         print(f'meet cond: A:[0, {a_contrib-1}], B:[0, {b_contrib-1}]')
        #         return self.get_median(A, 0, a_contrib - 1, B, 0, b_contrib - 1)

        # a_contrib -> num of elements of A contributes
        a_contrib_min = 1
        a_contrib_max = contrib_n
        a_contrib = (a_contrib_max + a_contrib_min) // 2

        while 1:
            assert a_contrib > 0

            b_contrib = contrib_n - a_contrib
            if b_contrib > len_B:
                # need expand a_contrib
                a_contrib_min = a_contrib + 1
                a_contrib = (a_contrib_max + a_contrib_min) // 2
                continue

            print(f'a contrib:{a_contrib}, b contrib: {b_contrib}')

            meet_cond, need_expand = self.meet_median_cond(A, 0, a_contrib - 1, B, 0, b_contrib - 1)
            if meet_cond:
                print(f'meet cond: A:[0, {a_contrib-1}], B:[0, {b_contrib-1}]')
                return self.get_median(A, 0, a_contrib - 1, B, 0, b_contrib - 1)
            else:
                if need_expand:
                    a_contrib_min = a_contrib + 1
                else:
                    # shrink a_contrib
                    a_contrib_max = a_contrib - 1

                a_contrib = (a_contrib_max + a_contrib_min) // 2

        assert False, 'Should never reach here!'
