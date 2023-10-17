class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        countT,window={},{}
        for c in t:
            countT[c]=1+ countT.get(c,0)
        left,have,need=0,0,len(countT)
        result,resultLen="", float('infinity')
        for right in range(len(s)):
            #Get new char
            newChar=s[right]
            #Update Window
            window[newChar]=1+window.get(newChar,0)
            #Check to see if char in count and then see if count is same
            if newChar in countT and countT[newChar]==window[newChar]:
                have+=1
            while have==need:
                if (right-left+1)<resultLen:
                    resultLen=right-left+1
                    result=s[left:right+1]
                window[s[left]]-=1
                if s[left] in countT and window[s[left]]<countT[s[left]]:
                    have -=1
                left+=1           
        return result