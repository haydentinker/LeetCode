class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        foundNums=set()
        for i in nums:
            if i in foundNums:
                return i
            foundNums.add(i)
        return 0