class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sPattern = {}
        tPattern ={}

        for i in range(len(s)):
            if(s[i] not in sPattern):
                sPattern[s[i]] = [i]
            if(t[i] not in tPattern):
                tPattern[t[i]] = [i]
            
            if sPattern[s[i]] != tPattern[t[i]]:
                return False
        return True