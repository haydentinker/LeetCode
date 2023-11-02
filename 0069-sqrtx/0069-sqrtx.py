class Solution:
    def mySqrt(self, x: int) -> int:
        count=0
        cur=1
        while x>=cur*cur:
            cur+=1
            count+=1
        return count