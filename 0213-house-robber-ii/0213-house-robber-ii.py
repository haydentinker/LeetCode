class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        firstRob1,firstRob2 =0,0
        secondRob1,secondRob2=0,0
        for n in range(len(nums)):
            if n<len(nums)-1:
                temp=max(firstRob1+nums[n],firstRob2)
                firstRob1=firstRob2
                firstRob2=temp
            if n>0:
                temp=max(secondRob1+nums[n],secondRob2)
                secondRob1=secondRob2
                secondRob2=temp
            
        return max(secondRob2,firstRob2)