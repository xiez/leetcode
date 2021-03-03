class Solution:
    def overlap(self, a, b):
        if a[1] >= b[0] and a[1] <= b[1]:
            return True

        if b[0] >= a[0] and b[0] <= a[1]:
            return True

        return False

    def merge_intervals(self, a, b):
        if a[1] >= b[0] and a[1] <= b[1]:
            a[1] = b[1]

        # if b[0] >= a[0] and b[0] <= a[1]:
        #     pass

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda e: e[0])

        i, j = 0, 1

        try:
            while 1:
                a = intervals[i]
                b = intervals[j]
                print(b)
                if self.overlap(a, b):
                    self.merge_intervals(a, b)
                    del intervals[j]
                else:
                    i += 1
                    j = i + 1
        except IndexError:
            pass

        return intervals
