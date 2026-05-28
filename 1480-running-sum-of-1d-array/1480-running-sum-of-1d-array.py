class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        preffix= 0
        for index, val in enumerate(nums):
            nums[index] += preffix
            preffix +=val
        return nums