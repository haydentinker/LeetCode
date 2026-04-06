class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacleSet = set()
        for o in obstacles:
            obstacleSet.add((o[0], o[1]))

        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0)
        ]

        x, y = 0, 0
        currDirection = 0 
        maxDist = 0
        for cmd in commands:
            if cmd == -1:
                currDirection = (currDirection + 1) % 4
            elif cmd == -2:
                currDirection = (currDirection + 3) % 4
            else:
                while cmd > 0: 
                    dx = x + directions[currDirection][0]
                    dy = y + directions[currDirection][1]

                    if (dx, dy ) in obstacleSet:
                        break
                    x = dx 
                    y = dy
                    maxDist = max(maxDist, x * x + y * y)
                    cmd -= 1
        return maxDist