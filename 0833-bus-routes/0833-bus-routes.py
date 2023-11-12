class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stopMap=defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                stopMap[stop].append(i)
        queue=[(0,source)]
        stopsVisited=set()
        routesVisited=set()
        while queue:
            stopCounter,curStop=heappop(queue)
            if curStop==target:
               return stopCounter
            if curStop not in stopsVisited:
                stopsVisited.add(curStop)
                for i in stopMap[curStop]:
                    if i not in routesVisited:
                        routesVisited.add(i)
                        for j in routes[i]:
                            if not j==curStop:
                                heappush(queue,(stopCounter+1,j))
        return -1
