class Solution:
    def sortVowels(self, s: str) -> str:
        vowels='AEIOUaeiou'
        heap=[]
        indexList=[]
        for i in range(len(s)):
            if s[i] in vowels:
                heappush(heap,s[i])
                
            else:
                indexList.append(i)
        result=""
        for i in range(len(s)):
            if i in indexList:
                result= result+s[i]
            else:
                result =result+heappop(heap)

        return result
