import math
class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]
    def addNum(self, num: int) -> None:
        if self.large and num>self.large[0]:
            heappush(self.large,num)
        else:
            heappush(self.small,-1*num)
        if len(self.small)>len(self.large)+1:
            val=heappop(self.small)
            heappush(self.large,-1*val)  
        if len(self.large)>len(self.small)+1:
            val=-1*heappop(self.large)
            heappush(self.small,val)
        
    def findMedian(self) -> float:
        if len(self.large)>len(self.small):
            return self.large[0]
        elif len(self.large)<len(self.small):
            return self.small[0]*-1
        return (self.large[0]-1*self.small[0])/2
       



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()