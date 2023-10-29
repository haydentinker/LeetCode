class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        #Suboptimal solution
        # def dfs(current):
        #     if len(current)>=len(nums):
        #         if current not in result:
        #             result.append(current)
        #         return 
        #     for i in nums:
        #         if i not in current:
        #             dfs(current+[i])
        #optimal solution
        if (len(nums)==1):
            return [nums.copy()]
        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result

        