class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result=0
        prev=float('inf')
        for index in range(len(s)):
            value=romanMap[s[index]]
            if prev<value:
                value-=2*prev
            
            result+=value
            prev=value
        return result
