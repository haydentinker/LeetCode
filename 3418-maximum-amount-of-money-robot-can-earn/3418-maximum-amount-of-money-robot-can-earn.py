from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])

        dp = [[float('-inf')] * 3 for _ in range(n)]

        for k in range(3):
            if coins[m-1][n-1] < 0 and k > 0:
                dp[n-1][k] = 0
            else:
                dp[n-1][k] = coins[m-1][n-1]

        for j in range(n - 2, -1, -1):
            for k in range(3):
                val = coins[m-1][j]
                take = val + dp[j+1][k]

                if val < 0 and k > 0:
                    dp[j][k] = max(take, dp[j+1][k-1])
                else:
                    dp[j][k] = take

        for i in range(m - 2, -1, -1):
            new_dp = [[float('-inf')] * 3 for _ in range(n)]

            for k in range(3):
                val = coins[i][n-1]
                take = val + dp[n-1][k]

                if val < 0 and k > 0:
                    new_dp[n-1][k] = max(take, dp[n-1][k-1])
                else:
                    new_dp[n-1][k] = take

            for j in range(n - 2, -1, -1):
                for k in range(3):
                    val = coins[i][j]

                    best_next = max(dp[j][k], new_dp[j+1][k])
                    take = val + best_next

                    if val < 0 and k > 0:
                        neutralize = max(dp[j][k-1], new_dp[j+1][k-1])
                        new_dp[j][k] = max(take, neutralize)
                    else:
                        new_dp[j][k] = take

            dp = new_dp

        return dp[0][2]
                