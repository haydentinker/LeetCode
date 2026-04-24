from collections import Counter
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counts = Counter(moves)
        res = counts['_'] + abs(counts['L'] - counts['R'])
        return res