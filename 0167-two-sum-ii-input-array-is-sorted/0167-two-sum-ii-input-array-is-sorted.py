class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # resultMap={}
        # for index,i in  enumerate(numbers):
        #     if i in resultMap.keys():
        #         return [resultMap[i],index+1]
        #     else:
        #         resultMap[target-i]=index+1
        left,right=0,len(numbers)-1
        while left<right:
            newSum=numbers[left]+numbers[right]
            if newSum>target:
                right-=1
            elif newSum<target:
                left+=1
            else:
                return [left+1,right+1]
        return []