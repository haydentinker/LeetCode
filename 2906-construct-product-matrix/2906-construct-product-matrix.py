class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        tot = 1
        MOD = 12345
        n, m = len(grid), len(grid[0])

        # Flatten grid
        arr = []
        for row in grid:
            for x in row:
                arr.append(x % MOD)

        N = len(arr)

        prefix = [1] * N
        suffix = [1] * N 
        for i in range(1, N):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD
        for i in range(N - 2, -1, -1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % MOD
        res = [[0] * m for _ in range(n)]
        index = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res[i][j] = (prefix[index] * suffix[index]) % MOD
                index +=1
  
        return res
        