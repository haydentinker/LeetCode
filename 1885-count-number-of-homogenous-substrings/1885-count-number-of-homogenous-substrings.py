class Solution:
    def countHomogenous(self, s: str) -> int:
        result=0
        l=0
        for index,currChar in enumerate(s):
            if s[l]==currChar:
                result+=index-l+1
            else:
                l=index
                result+=1
        return result %(10**9+7)