class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        numsDict = {}
        for i, value in enumerate(nums):
            if value in numsDict:
                numsDict[value].append(i)
            else:
                numsDict[value] = [i]
        ans = float('inf')
        for numsList in numsDict.values():
            if len(numsList) < 3:
                continue
            for i in range(len(numsList)-2):
                dist = 2 * (numsList[i+2]-numsList[i])
                ans = min(ans,dist)
        return -1 if ans == float('inf') else ans
        