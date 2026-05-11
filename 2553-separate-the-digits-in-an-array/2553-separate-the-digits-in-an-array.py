class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if i >= 10:
                for digit in str(i):
                    res.append(int(digit))
            else:
                res.append(i)
        return res
