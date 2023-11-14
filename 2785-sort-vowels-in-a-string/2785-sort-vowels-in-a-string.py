class Solution:
    def sortVowels(self, s: str) -> str:
        s=list(s)
        vowels='AEIOUaeiou'
        heap=[]
        indexList=[]
        for i in range(len(s)):
            if s[i] in vowels:
                heappush(heap,s[i])
                indexList.append(i)
                

        for i in range(len(heap)):
            s[indexList[i]]=heappop(heap)

        return "".join(s)
