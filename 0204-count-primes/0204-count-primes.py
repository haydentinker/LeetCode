class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        seen=set()
        result=0
        for i in range(2,n):
            if i not in seen:
                result+=1
                counter=i
                while counter<=n:
                    seen.add(counter)
                    counter+=i
        return result
            