class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums)<=2:
        #     return max(nums)
        # result=[0]*len(nums)
        # result[0]=nums[0]
        # result[1]=nums[1]
        # for i in range(2,len(nums)):
        #     if i<3:
        #         result[i]=nums[i]+result[i-2]
        #     else:
        #         result[i]=nums[i]+max(result[i-2],result[i-3])
    
        # return max(result[-2],result[-1])
        rob1,rob2 =0,0
        for n in nums:
            temp=max(rob1+n,rob2)
            rob1=rob2
            rob2=temp
        return rob2