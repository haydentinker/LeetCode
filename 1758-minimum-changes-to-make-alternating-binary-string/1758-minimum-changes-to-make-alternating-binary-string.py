class Solution:
    def minOperations(self, s: str) -> int:
        oneStartingCount, zeroStartingCount= 0,0
        for i in range(len(s)):
            expected1Pattern = '0' if i % 2 == 0 else '1'
            expected0Pattern = '1' if i % 2 == 0 else '0'
            if not s[i] == expected1Pattern:
                oneStartingCount +=1
            if not s[i] == expected0Pattern:
                zeroStartingCount +=1
        return min(oneStartingCount, zeroStartingCount)
