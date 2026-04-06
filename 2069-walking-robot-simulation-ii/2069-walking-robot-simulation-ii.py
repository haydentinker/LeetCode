from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.currentPosition = [0,0]
        self.currentDirection = 0
        self.directionMap = {
            0: "East",
            1: "North",
            2: "West",
            3: "South"
        }
        self.perim = 2*(self.width + self.height - 2)

    def step(self, num: int) -> None:
        #Eliminate loops and set direction to south when robot at starting position
        if num >= self.perim:
            num %= self.perim
            if self.currentPosition == [0,0] and self.currentDirection == 0:
                self.currentDirection = 3 
        while num > 0:
            if self.currentDirection == 0: 
                steps = min(num, self.width - self.currentPosition[0] - 1)
                num -= steps
                self.currentPosition[0] += steps
            elif self.currentDirection == 1:
                steps = min(num,self.height - self.currentPosition[1] -1 )
                num -= steps
                self.currentPosition[1] += steps
            elif self.currentDirection ==2:
                steps = min(num,self.currentPosition[0])
                num -= steps
                self.currentPosition[0] -= steps
            elif self.currentDirection ==3:
                steps = min(num,self.currentPosition[1])
                num -= steps
                self.currentPosition[1] -= steps

            if num > 0: #if there are left overs it needs to switch directions
                self.currentDirection = (self.currentDirection + 1) % 4
    def getPos(self) -> List[int]:
        return self.currentPosition

    def getDir(self) -> str:
        return self.directionMap[self.currentDirection]

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()