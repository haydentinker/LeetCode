class Solution:
    def judgeCircle(self, moves: str) -> bool:
        leftRight = 0
        upDown =  0
        for i in moves:
            if i == 'L':
                leftRight -= 1
            elif i == 'R':
                leftRight +=1
            elif i == 'U':
                upDown +=1
            else:
                upDown -=1
        return leftRight == 0 and upDown == 0
