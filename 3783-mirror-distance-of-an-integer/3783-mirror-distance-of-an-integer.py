class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverseNum(x):
            return int(str(x)[::-1])
        reversedN = reverseNum(n)
        return abs(n - reversedN)