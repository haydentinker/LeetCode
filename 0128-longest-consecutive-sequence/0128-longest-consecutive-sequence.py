class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(nums)
        longestSequence=1
        currSequence=1
        for index, value in enumerate(nums[1:], start=1):
            if value==nums[index-1]:
                continue
            if value==nums[index-1]+1:
                currSequence+=1
            else:
                currSequence=1
            if currSequence>longestSequence:
                longestSequence=currSequence

        return longestSequence