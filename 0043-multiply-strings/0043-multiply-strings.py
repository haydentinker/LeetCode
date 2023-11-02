class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1Int=self.convert(num1)
        num2Int=self.convert(num2)
        return str(num2Int*num1Int)

    
    def convert(self,num):
        vals={48:0,49:1,50:2,51:3,52:4,53:5,54:6,55:7,56:8,57:9}
        result=0
        place=1
        for i in range(len(num)-1,-1,-1):
            result+=vals[ord(num[i])]*place
            place*=10
        return result