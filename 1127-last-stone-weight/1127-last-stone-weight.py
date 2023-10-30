class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[-x for x in stones]
        heapify(maxHeap)
        while maxHeap:
            if len(maxHeap)==1:
                return -1*heappop(maxHeap)
            y=heappop(maxHeap)
            x=heappop(maxHeap)
            if not x==y:
                heappush(maxHeap,y-x)
        return 0