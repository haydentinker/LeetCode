class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.dummyLeft = Node(-1,-1)
        self.dummyRight = Node(-1,-1)
        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft
    def remove(self, node) -> None:
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
                   
    def add(self,node) -> None: 
        leader = self.dummyRight.prev
        leader.next, node.prev = node, leader
        self.dummyRight.prev, node.next = node, self.dummyRight

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].value
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.dummyLeft.next
            self.remove(lru)
            self.cache.pop(lru.key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)