class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #If its empty return 0
        if not nums:
            return 0
        # Sort array in order
        nums=sorted(nums)
        # Overall longest Sequence
        longestSequence=1
        # Current Longest Sequence
        currSequence=1
        #For each in nums starting at 1 
        for index, value in enumerate(nums[1:], start=1):
            #Check to see if it is the same as the previous number
            #If it is continue to next iteration
            if value==nums[index-1]:
                continue
            #Check to see if it is adding to the sequence and increments currentSequence
            elif value==nums[index-1]+1:
                currSequence+=1
            #Else reset the current sequence
            else:
                currSequence=1
            #Finally update longestSequence if currSequence is larger
            longestSequence=max(currSequence,longestSequence)

        return longestSequence