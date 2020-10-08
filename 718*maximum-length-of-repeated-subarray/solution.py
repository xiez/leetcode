class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        max_length = 0
        dp_table = [[-1] * (len(A) + 1) for _ in range(len(B) + 1)]

        for row in range(len(B) + 1):
            for col in range(len(A) + 1):
                if row == 0 or col == 0:
                    dp_table[row][col] = 0
                elif A[col-1] == B[row-1]:
                    dp_table[row][col] = 1 + dp_table[row-1][col-1]
                    max_length = max(max_length, dp_table[row][col])
                else:
                    dp_table[row][col] = 0

        return max_length

if __name__ == '__main__':
    s = Solution()
    print(s.findLength([1,2,3,2,1], [2,3,2,1,4,7]))
