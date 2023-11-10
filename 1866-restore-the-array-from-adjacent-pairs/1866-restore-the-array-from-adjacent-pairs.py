class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def dfs(vertex):
           visited.add(vertex)
           result.append(vertex)
           for val in adjacentDict[vertex]:
               if val not in visited:
                   dfs(val)
        adjacentDict=defaultdict(list)
        for i in adjacentPairs:
            adjacentDict[i[0]].append(i[1])
            adjacentDict[i[1]].append(i[0])
        for key,val in adjacentDict.items():
            if len(val)==1:
                start=key
                break
        
        visited=set()
        result=[]
        dfs(start)
    
        return result