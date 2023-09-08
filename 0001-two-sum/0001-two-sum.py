class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap={}
        for index,i in enumerate(nums):
            if i in myMap.keys():
                return([myMap[i],index])
    
            myMap[target-i]=index
        return []
