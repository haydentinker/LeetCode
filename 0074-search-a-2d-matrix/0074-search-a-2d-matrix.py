class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary search with additional rows
        bottom=0
        top=len(matrix)-1
        #Binary Search Rows 
        while bottom<=top:
            rowPartition=(bottom+top)//2
            left=0
            right=len(matrix[0])-1
            #Binary Search Columns
            while left<=right:
                colPartition=(left+right)//2
                if matrix[rowPartition][colPartition]==target:
                    return True
                elif matrix[rowPartition][colPartition]<target:
                    left=colPartition+1
                else:
                    right=colPartition-1
            if matrix[rowPartition][(left+right)//2]<target:
                bottom=rowPartition+1
            else:
                top=rowPartition-1
                    

        return False