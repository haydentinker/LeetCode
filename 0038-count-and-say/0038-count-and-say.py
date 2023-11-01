class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        prevString=self.countAndSay(n-1)
        index=0
        currString=""
        while index<len(prevString):
            count=1
            while index<len(prevString)-1 and prevString[index]==prevString[index+1]:
                index+=1
                count+=1
            currString=currString+str(count)+prevString[index]
            index+=1
        return currString
