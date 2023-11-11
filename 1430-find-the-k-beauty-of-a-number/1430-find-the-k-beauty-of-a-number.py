class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        result=0
        stringNum=str(num)
        l=0
        r=k-1
        while r<len(stringNum):
            window=int(stringNum[l:r+1])
            if not window==0 and num%window==0:
                result+=1
            l+=1
            r+=1
        
        return result