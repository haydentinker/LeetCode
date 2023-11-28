class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if corridor.count('S')<2:
            return 0
        mod=10e9+7
        seatCount=0
        positions=1
        plants=1
        for i in corridor:
            if seatCount>0 and seatCount%2==0:
                if i=='S':
                    positions*=plants
                    plants=1
                else:
                    plants+=1
            if i =='S':
                seatCount+=1
    
        return positions%(10**9+7) if seatCount>0 and seatCount%2==0 else 0