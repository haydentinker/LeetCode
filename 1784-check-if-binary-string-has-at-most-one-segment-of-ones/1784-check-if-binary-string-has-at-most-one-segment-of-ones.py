class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        indexOf0 = s.find('0')
        if(indexOf0 != -1):
            trimmedString = s[indexOf0:]
            if(trimmedString.find('1') != -1):
                return False
        return True