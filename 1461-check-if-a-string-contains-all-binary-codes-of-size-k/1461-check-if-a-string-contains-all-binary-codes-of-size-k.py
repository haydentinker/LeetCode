class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        needed = 1 << k
        num = 0
        mask = needed - 1  
        for i in range(len(s)) :
            num = ((num << 1) & mask) | int(s[i])
            if i >= k -1:
                seen.add(num)
                if len(seen) == needed:
                    return True
        return False