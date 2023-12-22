class Solution:
    def maxScore(self, s: str) -> int:
        result = -inf
        zeros=0
        ones=0
        for i in range(len(s)-1):
            if s[i]=='0':
                zeros+=1
            else:
                ones+=1
            result=max(result,zeros-ones)
        
        if s[-1]=='1':
            ones+=1
        
        
        return result+ones