class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols=len(matrix)
        rows=len(matrix[0])
        zeroRows=[]
        zeroCols=[]
        for i in range(cols):
            for j in range(rows):
                if matrix[i][j]==0:
                    zeroRows.append(j)
                    zeroCols.append(i)
        for i in zeroRows:
            for col in range(cols):
                matrix[col][i]=0
        for i in zeroCols:
            for row in range(rows):
                matrix[i][row]=0

