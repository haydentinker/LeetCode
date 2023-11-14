class Solution:
    def climbStairs(self, n: int) -> int:
        # def climb(curNum):
        #     if n-curNum<=1:
        #         return 1
        #     return climb(curNum+1)+climb(curNum+2)
        # return climb(0)
        if n <=3:
            return n
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]