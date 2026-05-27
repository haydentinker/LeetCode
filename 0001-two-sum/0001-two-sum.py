class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i, num in enumerate(nums):
            if num in numsDict:
                return [numsDict[num], i]
            else:
                numsDict[target - num] = i 
        return -1