class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        suffix = sum(nums)

        prefix = 0
        res = []
        for i in range(len(nums)):
            suffix -= nums[i]
            res.append(abs(prefix - suffix))
            prefix += nums[i]

        return res