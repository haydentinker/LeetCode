class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force Method
        # for i in range(len(nums)):
        #     newEntry=1
        #     for index,j in enumerate(nums):
        #         if (index==i):
        #             pass
        #         else:
        #             newEntry*=j
        #     result.append(newEntry)
        result=[]
        prefix=1
        for num in nums:
            prefix*=num
            result.append(prefix)
        postfix=1
        for i in range(len(nums)-1,0,-1):
            result[i]=postfix*result[i-1]
            postfix*=nums[i]
        result[0]=postfix

        return result