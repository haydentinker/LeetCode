class Solution:
   def productExceptSelf(self, nums):
        n = len(nums)
        res = []
        prefix = 1
        suffix = 1

        for i in range(0, n):
            prefix *= nums[i]
            res.append(prefix)

        for i in range(n-1, 0, -1):
            res[i] = suffix * res[i-1]
            suffix *= nums[i]
        res[0] = suffix

        return res
