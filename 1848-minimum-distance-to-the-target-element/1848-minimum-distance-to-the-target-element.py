class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minDistance = float('inf')
        for i, num in enumerate(nums):
            if num == target:
                minDistance = min(minDistance, abs(i - start))
        return minDistance