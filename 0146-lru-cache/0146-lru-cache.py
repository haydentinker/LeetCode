class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        #Left is least recently used and right is most recently used
        self.dummyLeft,self.dummyRight=Node(0,0),Node(0,0)
        self.dummyLeft.next, self.dummyRight.prev= self.dummyRight,self.dummyLeft
        self.cacheMap={}
        # self.keyList=[]
    #Suboptimal solution
    # def get(self, key: int) -> int:
    #     getCacheValue=self.cacheMap.get(key,-1)
    #     print(getCacheValue)
    #     if getCacheValue>-1:
    #         self.keyList.remove(key)
    #         self.keyList.append(key)
    #     return getCacheValue
    # def put(self, key: int, value: int) -> None:
    #     if key in self.cacheMap.keys():
    #         self.cacheMap[key]=value
    #         self.keyList.remove(key)
    #         self.keyList.append(key)
    #     else:
    #         if len(self.keyList)>=self.capacity:
    #             removedItem=self.keyList.pop(0)
    #             self.cacheMap.pop(removedItem)
    #         self.keyList.append(key)
    #         self.cacheMap[key]=value
        #Optimal Solution using Double Linked List
    def remove(self,node):
        prevNode, nextNode=node.prev, node.next
        prevNode.next, nextNode.prev=nextNode,prevNode

    def insert(self,node):
        prevNode=self.dummyRight.prev
        prevNode.next=node
        self.dummyRight.prev=node
        node.next=self.dummyRight
        node.prev=prevNode
    def get(self, key: int) -> int:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
            self.insert(self.cacheMap[key])
            return self.cacheMap[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
        self.cacheMap[key]=Node(key,value)
        self.insert(self.cacheMap[key])
        if len(self.cacheMap)>self.capacity:
            leastRecentlyUsed=self.dummyLeft.next
            self.remove(leastRecentlyUsed)
            del self.cacheMap[leastRecentlyUsed.key]
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)