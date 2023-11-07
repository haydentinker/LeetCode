class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        monstersKilled=0
        monsters=[]
        for i in range(len(dist)):
            heappush(monsters,(dist[i]/speed[i],speed[i]))
        while monsters:
            currMonster=heappop(monsters)
            if currMonster[0]*currMonster[1]-currMonster[1]*monstersKilled<=0:
                break
            else:
                monstersKilled+=1

        return monstersKilled

