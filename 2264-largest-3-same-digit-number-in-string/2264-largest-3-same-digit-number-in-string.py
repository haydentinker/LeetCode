class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result="-1"
        l,r=0,2
        while r<len(num):
            if num[l]==num[r] and num[l]==num[r-1]:
                if num[l:r+1]>result:
                    result=num[l:r+1]
            l+=1
            r+=1
               
        return result if not result=="-1" else ""

