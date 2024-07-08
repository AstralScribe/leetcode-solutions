from typing import List
import time

# Solution #1
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        blocks = self.get_semiboard(board)
        columns = self.get_columns(board)

        for i in range(9):
            cols = columns[i].replace(".","")
            rows = "".join(board[i]).replace(".","")
            block = "".join(blocks[i]).replace(".", "")
            
            if len(cols) != len(set(cols)):
                return False

            if len(rows) != len(set(rows)):
                return False

            if len(block) != len(set(block)):
                return False

        return True


    def get_semiboard(self, board):
        temp = []
        for i in range(3):
            for j in range(3):
                t = []
                for k in range(3):
                    t.extend(board[i*3:i*3+3][k][j*3:j*3+3])
                temp.append(t)
        return temp
        
    def get_columns(self, board):
        temp = {}
        for i in board:
            for j in range(9):
                temp[j] = temp.get(j, "") + i[j]
        return list(temp.values())


# Solution #2
class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = {}
        cols = {}
        blks = {}

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                b = str(i//3)+str(j//3)

                rows[i] = rows.get(i, set())
                cols[j] = cols.get(j, set())
                blks[b] = blks.get(b, set())

                if val == ".":
                    continue
                if val in rows[i] or val in cols[j] or val in blks[b]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                blks[b].add(val)

        return True


def run_test(board):
    s = Solution()
    chk = s.isValidSudoku(board)
    return chk
    

if __name__ == "__main__":
    board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    tick = time.perf_counter()
    chk = run_test(board)
    tock = time.perf_counter()
    print(f"Valid: {chk}")
    print(f"Time: {tock-tick}")
