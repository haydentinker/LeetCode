from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        tCount = Counter(t)
        have, need = 0, len(tCount)
        left = 0 
        count = {}
        resLength= float('inf')
        res = [-1,-1]
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0 ) + 1
            if s[right] in tCount and count[s[right]] == tCount[s[right]]:
                have +=1 

            while have == need:
               
                if (right - left +1 ) < resLength:
                    res = [left, right]
                    resLength = right - left + 1
                count[s[left]] -= 1 
                if s[left] in tCount and count[s[left]] < tCount[s[left]]:
                    have -=1
                left +=1
        l, r = res 
        return s[l: r+1]