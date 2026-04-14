class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        #sort
        robot.sort()
        factory.sort()
        slots = []
        for pos, limit in factory:
            slots.extend([pos] * limit)
        n = len(robot)
        m = len(slots)
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(m+1):
            dp[0][i] = 0 

        for i in range(1,n+1):
            for j in range(1,m+1):
                cost = abs(robot[i - 1] - slots[j - 1])

                dp[i][j] = min(dp[i][j-1], dp[i-1][ j-1]+cost)

        return dp[n][m]