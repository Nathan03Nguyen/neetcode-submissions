class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_di = set() # (r + c)
        neg_di = set() # (r - c)

        res = []
        board = [['.'] * n  for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r + c) in pos_di or (r - c) in neg_di:
                    continue

                col.add(c)
                pos_di.add(r + c)
                neg_di.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                pos_di.remove(r + c)
                neg_di.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res