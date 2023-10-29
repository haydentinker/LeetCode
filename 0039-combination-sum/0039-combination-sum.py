class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        current=[]
        def sum(index,currentSum):
            print(current)
            if currentSum==target:
                result.append(current.copy())
                return
            if currentSum>target or index>=len(candidates):
                return
            current.append(candidates[index])
            sum(index,currentSum+candidates[index])
            current.pop()
            sum(index+1,currentSum)
                

        
        sum(0,0)
        return result