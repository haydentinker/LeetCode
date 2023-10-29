class TrieNode:
    def __init__(self):
        self.children={}
        self.isCompleteWord=False
class Solution:
    def __init__(self):
        self.Trie=TrieNode()
        self.result=[]
    def insert(self, word: str) -> None:
        current=self.Trie
        for i in word:
            if i not in current.children:
                current.children[i]=TrieNode()
            current=current.children[i]
        current.isCompleteWord=True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #Word Search 1 Solution
        result=set()
        rows=len(board)
        cols=len(board[0])
        path=set()
        def search(current,indexI,indexJ,word):
            if current.isCompleteWord:
                result.add(word)
            
            if (indexI<0 or indexJ<0 or 
                indexI >=rows or indexJ>=cols or 
                board[indexI][indexJ] not in current.children or 
                (indexI,indexJ) in path):
            
                return
        
            path.add((indexI,indexJ))
            currChar=board[indexI][indexJ]
            word=word+currChar
    
         
            search(current.children[currChar],indexI,indexJ-1,word)
            search(current.children[currChar],indexI,indexJ+1,word) 
            search(current.children[currChar],indexI-1,indexJ,word)  
            search(current.children[currChar],indexI+1,indexJ,word)
            path.remove((indexI,indexJ))
            
        for i in words:
            self.insert(i)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in self.Trie.children:
                    search(self.Trie,i,j,"")
        return result