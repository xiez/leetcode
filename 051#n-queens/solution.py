import copy

DEBUG = False

def log(msg):
    if DEBUG:
        print(msg)

class Solution(object):
    def generate_board(self, n):
        b = []
        for i in range(n):
            b.append([0] * n)

        return b

    def board_to_str(self, board):
        ret = []
        for row in board:
            s = ""
            for e in row:
                if e == 1:
                    s += "Q"
                else:
                    s += "."
            ret.append(s)
        return ret

    def board_SE(self, board, row, col):
        """South-East of current point on the board"""
        ret = []
        while True:
            row += 1
            col += 1
            if row < 0 or col < 0:
                break
            try:
                ret.append(board[row][col])
            except IndexError:
                break
        return ret

    def board_SW(self, board, row, col):
        ret = []
        while True:
            row += 1
            col -= 1
            if row < 0 or col < 0:
                break
            try:
                ret.append(board[row][col])
            except IndexError:
                break
        return ret

    def board_NE(self, board, row, col):
        ret = []
        while True:
            row -= 1
            col += 1
            if row < 0 or col < 0:
                break
            try:
                ret.append(board[row][col])
            except IndexError:
                break
        return ret

    def board_NW(self, board, row, col):
        ret = []
        while True:
            row -= 1
            col -= 1
            if row < 0 or col < 0:
                break
            try:
                ret.append(board[row][col])
            except IndexError:
                break
        return ret

    def board_diag(self, board, row, col):
        ret = []
        for d_row, d_col in [(1,1), (1,-1), (-1, 1), (-1,-1)]:
            tmp_row = row
            tmp_col = col

            while True:
                tmp_row += d_row
                tmp_col += d_col
                if tmp_row < 0 or tmp_col < 0:
                    break
                try:
                    ret.append(board[tmp_row][tmp_col])
                except IndexError:
                    break
        return ret

    def check_clash(self, board, row, col):
        if 1 in board[row]:
            return True

        # if 1 in self.board_SE(board, row, col):
        #     return True
        # if 1 in self.board_SW(board, row, col):
        #     return True
        # if 1 in self.board_NE(board, row, col):
        #     return True
        # if 1 in self.board_NW(board, row, col):
        #     return True

        if 1 in self.board_diag(board, row, col):
            return True

        return False

    def get_queen_pos_by_column(self, board, col):
        row = 0
        try:
            while True:
                if board[row][col] == 1:
                    return (row, col)
                else:
                    row += 1
        except IndexError:
            return None

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ret = []

        board = self.generate_board(n)

        col = 0
        row = 0
        while col < n:
            end_row = True

            while row < n:
                if self.check_clash(board, row, col) is True:
                    # try next row in this column until reach the end ..
                    # backtrack to previous column ..
                    # try next row until reach the end
                    log('try %s,%s ...  clash! try next row..' % (row, col))
                    row += 1
                    continue
                else:
                    end_row = False
                    log('try %s,%s ...  ok! play queen at %s, %s' % (row, col, row, col))
                    board[row][col] = 1
                    log(board)

                    if col == n - 1:
                        ret.append(copy.deepcopy(board))
                        log('Find a solution, append to ret, %s' % ret)

                        log('reset %s,%s to 0' % (row, col))
                        board[row][col] = 0
                        # stay in current column, goto next row
                        row += 1
                    else:
                        # goto next column, starts with first row
                        col += 1
                        row = 0
                        break

            if end_row:
                col -= 1
                if col < 0:
                    break

                try:
                    prev_row, prev_col = self.get_queen_pos_by_column(board, col)
                except TypeError:
                    break

                row = prev_row + 1
                log('backtracking.. goto previous column %s and next row %s' % (col, row))
                if col == 0 and row >= n:
                    log('Finished..')
                    break

                log('reset prev row, col: %s,%s to 0' % (prev_row, prev_col))
                board[prev_row][prev_col] = 0

        r = []
        for board in ret:
            r.append(self.board_to_str(board))

        return r

if __name__ == '__main__':
    s = Solution()
    # print(len(s.solveNQueens(1)))
    # assert len(s.solveNQueens(5)) == 10

    # board = [[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]]
    # print(s.board_diag(board, 0, 2))

    print('Done')
