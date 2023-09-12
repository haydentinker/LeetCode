class Solution:
    def canEat(self,piles,h,speed):
        x=sum([ceil(pile/speed) for pile in piles])
        return x<=h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left= ceil(min(piles) / h)
        right=max(piles)
        while left<right:
            mid = (left+right) >> 1
            if self.canEat(piles,h,mid):
                right=mid
            else:
                left=mid+1
        
        return left
    