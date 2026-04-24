from collections import Counter
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counts = Counter(moves)
        res = counts['_']
        if counts['L'] > counts['R']:
            res += counts['L'] - counts['R']
        else:
            res += counts['R'] - counts['L']
        return res