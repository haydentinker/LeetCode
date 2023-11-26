class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        for j in range(m):
            for i in range(1,n):
                if matrix[i][j]:
                    matrix[i][j]+=matrix[i-1][j]
        result=0
        for i in range(n):
            matrix[i].sort()
            for j in range(m-1,-1,-1):
                if matrix[i][j]==0:
                    break
                result = max(result, (m-j)*matrix[i][j])
        return result 
            