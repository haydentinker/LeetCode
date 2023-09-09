class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        result=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:    
                continue
            j=i+1
            k=n-1
            while j<k:
                sum=nums[i]+nums[k]+nums[j]
                if sum==0:
                    result.append([nums[i],nums[k],nums[j]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1

                    while k>j and nums[k]==nums[k+1]:
                        k-=1
                elif sum>0:
                    k-=1
                else:
                    j+=1
        return(result)