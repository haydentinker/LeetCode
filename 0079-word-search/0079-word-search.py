class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])

        path=set()
        def search(wordIndex,indexI,indexJ):
            if wordIndex == len(word):
                return True
            if (indexI<0 or indexJ<0 or 
                indexI >=rows or indexJ>=cols or 
                board[indexI][indexJ] != word[wordIndex] or 
                (indexI,indexJ) in path):
                return False
        
            path.add((indexI,indexJ))
          
            result = (
                search(wordIndex+1,indexI,indexJ-1) or 
                search(wordIndex+1,indexI,indexJ+1) or 
                search(wordIndex+1,indexI-1,indexJ) or 
                search(wordIndex+1,indexI+1,indexJ))
            path.remove((indexI,indexJ))
            return result
        for i in range(rows):
            for j in range(cols):
                    if search(0,i,j): return True
        return False