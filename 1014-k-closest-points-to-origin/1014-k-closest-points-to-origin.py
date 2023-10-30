import queue

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result=[]
        prio_q=queue.PriorityQueue()
        for point in points:
            distance=((0-point[0])**2+(0-point[1])**2)**.5
            prio_q.put((distance,point))
        for i in range(k):
            result.append(prio_q.get()[1])
        return result
        