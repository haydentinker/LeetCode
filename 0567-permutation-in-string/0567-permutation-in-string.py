class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len, s2Len = len(s1) , len(s2)
        if s1Len > s2Len:
            return False
        s1Chars, window = [0] *26, [0] *26
        for i in range(s1Len):
            s1Chars[ord(s1[i]) - ord('a')] +=1
            window[ord(s2[i])-ord('a')] +=1
        
        if s1Chars == window:
            return True

        for i in range(s2Len - s1Len):
            window[ord(s2[i])- ord('a')] -=1
            window[ord(s2[s1Len + i]) - ord('a')] +=1

            if window == s1Chars:
                return True
        return False

