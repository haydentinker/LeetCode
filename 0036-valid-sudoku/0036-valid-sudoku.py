class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result=[]
        for i in range(9):
            for j in range(9):
                element=board[i][j]
                if not element=='.':
                    result+=[(element,i),(j,element),(element,i//3,j//3)]
        return len(result)==(len(set(result)))