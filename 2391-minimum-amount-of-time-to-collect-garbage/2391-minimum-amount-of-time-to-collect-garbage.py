class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        result=0
        trucks={'G':-1,'P':-1,'M':-1}
        for i in range(len(garbage)):
            for truck in trucks.keys():
                countTruck=garbage[i].count(truck)
                if countTruck>0:
                    result+=countTruck
                    trucks[truck]=i
                    
        for i in trucks.values():
            if i>-1:
                result+=sum(travel[0:i])

        return result