class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sIndex = 0
        tIndex = 0 
        while sIndex < len(s) and tIndex < len(t):
            if s[sIndex] == t[tIndex]:
                sIndex +=1
            tIndex +=1
        print(sIndex, tIndex)
        return True if sIndex >= len(s) else False