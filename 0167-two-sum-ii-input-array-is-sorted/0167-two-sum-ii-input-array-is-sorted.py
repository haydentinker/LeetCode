class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        resultMap={}
        for index,i in  enumerate(numbers):
            if i in resultMap.keys():
                return [resultMap[i],index+1]
            else:
                resultMap[target-i]=index+1
        return []