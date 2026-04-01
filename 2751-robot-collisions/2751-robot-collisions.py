class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(len(positions))]) #sort robots positions and health
        stack = []

        robots = [list(r) for r in robots]

        for i in range(len(robots)):
            if robots[i][2] == 'R':
                stack.append(i)
            else:
                while stack and robots[i][1] > 0: #simulate collisons when robot is moving left
                    j = stack[-1]
                    if robots[j][1] < robots[i][1]: #robot[j] has less health
                        stack.pop()
                        robots[j][1] = 0
                        robots[i][1] -=1
                    elif robots[j][1] > robots[i][1]: #robot[i] has less health
                        robots[j][1] -= 1
                        robots[i][1] = 0 
                        break
                    else: #remove both if they are equal health
                        robots[j][1] = 0 
                        robots[i][1] = 0 
                        stack.pop()
                        break
        res = sorted([(r[3], r[1]) for r in robots if r[1] > 0]) #remove dead robots and sort by index and health
        return [h for _, h in res]