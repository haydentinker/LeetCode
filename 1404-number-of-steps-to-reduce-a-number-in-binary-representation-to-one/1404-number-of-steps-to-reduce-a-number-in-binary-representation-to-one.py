class Solution:
    def numSteps(self, s: str) -> int:
        return self.process(int(s,2),0,{})
    def process(self, num: int, steps: int, cache) -> int:
        if num in cache:
            return cache[num]
        if num == 1 :
            return steps
        if num % 2 == 0:
            res = self.process(num // 2, steps+1, cache)
            cache[num] = res
            return res
        else:
            res = self.process(num + 1, steps+1, cache)
            cache[num] = res
            return res