class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == -1:
                return 0
            
            i = ord(a) - ord('A')
            j = ord(b) - ord('A')
            
            r1, c1 = i // 6, i % 6
            r2, c2 = j // 6, j % 6
            
            return abs(r1 - r2) + abs(c1 - c2)
        n = len(word)
        dp = [ [inf]*27 for _ in range(n) ] 
        # Only need to track l and r state because one finger will be at word[-1]
        for j in range(27):
            dp[0][j] = 0

        for i in range(1, n):
            prev = word[i - 1]
            curr = word[i]

            for j in range(27):
                if dp[i - 1][j] == float('inf'):
                    continue
                dp[i][j] = min(
                    dp[i][j],
                    dp[i - 1][j] + dist(prev, curr)
                )
                dp[i][ord(prev) - ord('A')] = min(
                    dp[i][ord(prev) - ord('A')],
                    dp[i - 1][j] + dist(chr(ord('A') + j), curr)
                )

        return min(dp[n - 1])