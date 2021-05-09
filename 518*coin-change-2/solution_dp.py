class Solution:
    def change(self, amount, coins):
        rows = amount + 1
        cols = len(coins) + 1
        matrix = [[-1 for _ in range(cols)] for _ in range(rows)]

        i = 0
        while i < cols:
            matrix[0][i] = 1
            i += 1

        i = 1
        while i < rows:
            matrix[i][0] = 0
            i += 1

        r, c = 1, 1
        while r < rows:
            while c < cols:
                matrix[r][c] = matrix[r][c-1]
                tmp = r - coins[c-1]
                if tmp >= 0:
                    matrix[r][c] += matrix[tmp][c]

                c += 1
            r += 1
            c = 1

        return matrix[rows-1][cols-1]

if __name__ == '__main__':
    s = Solution()

    assert s.change(10, [1,5,10]) == 4
    assert s.change(50, [1,5,10,50]) == 37
