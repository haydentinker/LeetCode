class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result=[]
        leftSum=0
        leftCount=0
        rightCount=len(nums)
        rightSum=sum(nums)
        for num in nums:
            rightSum-=num
            rightCount-=1
            result.append(
                (num*leftCount-leftSum)+(rightSum-num*rightCount)
            )
            leftSum+=num
            leftCount+=1

        return result
