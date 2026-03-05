class Solution:
    def __init__(self):
        self.cache = {}

    def minOperations(self, s: str) -> int:
        return min(self.calculate(s, 0, '0'), self.calculate(s, 0, '1'))
    def calculate(self, s, i, expected):
            if i == len(s):
                return 0

            key = (i, expected)
            if key in self.cache:
                return self.cache[key]

            flip = 0 if s[i] == expected else 1
            next_expected = '1' if expected == '0' else '0'

            res = flip + self.calculate(s, i + 1, next_expected)
            self.cache[key] = res
            return res