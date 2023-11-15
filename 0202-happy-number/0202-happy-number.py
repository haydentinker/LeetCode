class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while True:
            curr=0
            for i in str(n):
                curr+=int(i)*int(i)
            if curr==1:
                return True
            elif curr in seen:
                return False
            seen.add(curr)
            n=curr