class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        j = len(colors)

        for i in range(j):
            if (colors[i] ^ colors[-1]) | (colors[-1 - i] ^ colors[0]):
                return j - 1 - i

        return 0