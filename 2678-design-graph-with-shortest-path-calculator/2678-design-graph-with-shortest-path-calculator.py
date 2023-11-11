class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph=defaultdict(list)
        for i in edges:
            self.graph[i[0]].append((i[1],i[2]))
    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1],edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        queue=[(0,node1)]
        visited=set()
        while queue:
            cost,currNode=heappop(queue)
            if currNode==node2:
                return cost
            if currNode not in visited:
                visited.add(currNode)
                for neighbor, edge_cost in self.graph[currNode]:
                    new_cost=cost+edge_cost
                    heappush(queue,(new_cost,neighbor))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)