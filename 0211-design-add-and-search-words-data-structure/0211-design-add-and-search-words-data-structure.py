class TrieNode:
    def __init__(self):
        self.children={}
        self.isCompleteWord=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
    def addWord(self, word: str) -> None:
        current=self.root
        for i in word:
            if i not in current.children:
                current.children[i]=TrieNode()
            current=current.children[i]
        current.isCompleteWord=True


    def search(self, word: str) -> bool:
        def searchByIndex(current,index,numberOfStars):
            if index>=len(word):
                return current.isCompleteWord
            currChar=word[index]
            if currChar in current.children:
                return searchByIndex(current.children[currChar],index+1,numberOfStars)
            elif currChar is "." and numberOfStars<2:
                for i in current.children:
                    result=searchByIndex(current.children[i],index+1,numberOfStars+1)
                    if result:
                        return True
            return False
        return searchByIndex(self.root,0,0)
        # current=self.root
        # for i in word:
        #     children=current.children
        #     if i is ".":
        #         for j in current.children:
        #             word=word.replace(i,j)
        #             if self.search(word):
        #                 return True
        #     if i not in children:
        #         return False
        #     current=current.children[i]
        
        # return current.isCompleteWord

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)