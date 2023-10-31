class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        positiveDiag=set()
        negativeDiag=set()
        cols=set()
        res=[]
        board=[['.']*n for i in range(n)]
        def backtrack(row):
            if row==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for i in range(n):
                if not (i in cols)and (not (row-i) in negativeDiag) and (not (row+i) in positiveDiag):
                    positiveDiag.add(row+i)
                    negativeDiag.add(row-i)
                    cols.add(i)
                    board[row][i]="Q"
                    backtrack(row+1)
                    board[row][i]="."
                    positiveDiag.remove(row+i)
                    negativeDiag.remove(row-i)
                    cols.remove(i)
            return     
    
        backtrack(0)
        return res