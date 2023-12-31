class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        cache={}
        result=-1
        for i in range(len(s)):
            if s[i] in cache:
                if i-cache[s[i]]==1:
                    result=max(result,0)
                else:
                    result=max(result,len(s[cache[s[i]]+1:i]))
            else:
                cache[s[i]]=i
            
        return result