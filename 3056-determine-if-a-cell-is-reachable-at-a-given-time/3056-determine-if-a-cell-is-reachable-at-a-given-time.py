class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and fy==sy:
            return not t==1
        distanceX=abs(fx-sx)
        distanceY=abs(fy-sy)
        minDistance=min(distanceX,distanceY)
        distanceX-=minDistance
        distanceY-=minDistance
        

        return distanceX<=t-minDistance and distanceY<=t-minDistance