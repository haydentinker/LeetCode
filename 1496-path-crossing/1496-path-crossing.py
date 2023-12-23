class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x=0
        y=0
        seen=set()
        seen.add((x,y))
        for i in path:
            if i=='N':
                y+=1
            elif i=='S':
                y-=1
            elif i=='E':
                x+=1
            else:
                x-=1
            if (x,y) in seen:
                return True
            print(x,y)
            seen.add((x,y))
        return False