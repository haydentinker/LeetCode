from collections import Counter
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        for i in range(len(s2) - k +1):
            substring = s2[i:i+k]
            if Counter(s1) == Counter(substring):
                return True
        return False