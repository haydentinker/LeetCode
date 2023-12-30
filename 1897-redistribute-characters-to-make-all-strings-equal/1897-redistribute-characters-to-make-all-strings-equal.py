class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count={}
        for word in words:
            for letter in word:
                count[letter]=count.get(letter,0)+1
        for i in count:
            if count[i]%len(words)!=0:
                return False 
        return True