class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]

        def dfs(current):
            if len(current)>=len(nums):
                if current not in result:
                    result.append(current)
                return 
            for i in nums:
                if i not in current:
                    dfs(current+[i])

        dfs([])
        return result