class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2

        for layer in range(num_layers):
            top, bottom = layer, m - 1 - layer
            left, right = layer, n - 1 - layer

            ring = []

            for c in range(left, right + 1):
                ring.append(grid[top][c])

            for r in range(top + 1, bottom + 1):
                ring.append(grid[r][right])

            for c in range(right - 1, left - 1, -1):
                ring.append(grid[bottom][c])

            for r in range(bottom - 1, top, -1):
                ring.append(grid[r][left])

            length = len(ring)
            shift = k % length
            ring = ring[shift:] + ring[:shift]

            i = 0
            for c in range(left, right + 1):
                grid[top][c] = ring[i]; i += 1
            for r in range(top + 1, bottom + 1):
                grid[r][right] = ring[i]; i += 1
            for c in range(right - 1, left - 1, -1):
                grid[bottom][c] = ring[i]; i += 1
            for r in range(bottom - 1, top, -1):
                grid[r][left] = ring[i]; i += 1

        return grid