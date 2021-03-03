class Solution:
    def overlap(self, a, b):
        if a is None or b is None:
            return False

        if a[1] >= b[0] and a[1] <= b[1]:
            return True

        if b[0] >= a[0] and b[0] <= a[1]:
            return True

        return False

    def merge_intervals(self, a, b):
        if a is None or b is None:
            return

        if a[1] >= b[0] and a[1] <= b[1]:
            a[1] = b[1]

    def merge(self, intervals):
        intervals.sort(key=lambda e: e[0])
        i, j = 0, 1
        l = len(intervals)

        while i < l:
            while j < l:
                a = intervals[i]
                b = intervals[j]
                # print('check overlap: %d, %d, %s, %s' % (i, j, a, b))
                if self.overlap(a, b):
                    # print('overlap: %s %s' % (a, b))
                    self.merge_intervals(a, b)
                    intervals[j] = None
                    j += 1
                else:
                    # print('NOT overlap: %s %s' % (a, b))
                    j = l

            i += 1
            j = i + 1
        # print(intervals)
        return [e for e in intervals if e is not None]

if __name__ == '__main__':
    # l = [[1,3],[2,6],[8,10],[15,18]]
    l = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
    s = Solution()

    ret = s.merge(l)
    print(ret)

    # assert s.overlap([4,6], [5,7]) is True
