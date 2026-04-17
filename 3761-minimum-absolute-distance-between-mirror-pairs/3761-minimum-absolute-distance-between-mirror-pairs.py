class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverseNum(x):
            return int(str(x)[::-1])

        lastSeen = {}
        res = float('inf')

        for j, value in enumerate(nums):
            if value in lastSeen:
                res = min(res, j - lastSeen[value])

            rev = reverseNum(value)
            lastSeen[rev] = j

        return res if res != float('inf') else -1