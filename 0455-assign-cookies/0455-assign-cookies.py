class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result=0
        g.sort()
        s.sort()
        child=0
        cookie=0
        while child<len(g) and cookie<len(s):
            if s[cookie]>=g[child]:
                result+=1
                child+=1    
            cookie+=1
        return result