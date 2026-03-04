class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowCountDict = {}
        colCountDict = {}
        indexOf1 = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    newRowCount = rowCountDict.get(i,0) + 1
                    newColCount = colCountDict.get(j,0) + 1
                    rowCountDict[i] = newRowCount
                    colCountDict[j] = newColCount
                    indexOf1 = indexOf1 + [(i,j)]
        ans = 0 
        for index in indexOf1:
            rowCount = rowCountDict.get(index[0])
            colCount = colCountDict.get(index[1])
            if rowCount == 1 and colCount ==1 :
                ans +=1
        return ans