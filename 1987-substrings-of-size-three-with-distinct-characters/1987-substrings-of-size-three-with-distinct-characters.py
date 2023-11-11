class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result=0
        currString=[]
        for index in range(0,len(s)):
          
            while s[index] in currString or len(currString)>=3:
                currString.pop(0)
            currString.append(s[index])
            if len(currString)==3:
                result+=1
                
            
            

        return result