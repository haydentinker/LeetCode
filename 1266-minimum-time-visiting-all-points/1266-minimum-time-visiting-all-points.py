class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result=0
        for i in range(len(points)-1):
            currPoint=points[i]
            nextPoint=points[i+1]
            result+=max(abs(nextPoint[0]-currPoint[0]),abs(nextPoint[1]-currPoint[1]))
            # xDifference=abs(nextPoint[0]-currPoint[0])
            # yDifference=abs(nextPoint[1]-currPoint[1])
            # if abs(xDifference-yDifference):
            #     while xDifference and yDifference:
            #         result+=1
            #         xDifference-=1
            #         yDifference-=1
            #     result+=yDifference+xDifference
            # else:
            #     result+=xDifference
                
        return result