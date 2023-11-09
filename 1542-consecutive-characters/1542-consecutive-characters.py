class Solution:
    def maxPower(self, s: str) -> int:
        result=1 
        currResult=1
        prev=" "
        for i in range(len(s)):
            if s[i]==prev:
                currResult+=1
                result=max(currResult,result)
            else:
                currResult=1
                prev=s[i]


        return result