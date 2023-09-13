class TimeMap:
  def __init__(self):
    self.store = {} 

  def set(self, key: str, value: str, timestamp: int) -> None:
    #if key in the map create and then append value and timestamp list
    if key not in self.store:
      self.store[key] = []
    self.store[key].append([value, timestamp])

  def get(self, key: str, timestamp: int) -> str:
    res = "" 
    #Get the list of values based on key
    values = self.store.get(key, []) 
    #Init high and low
    low, high = 0, len(values) - 1
    #Binary Search Time
    while low <= high:
      mid = (low + high) // 2
      #Return if we found the value
      if values[mid][1]==timestamp:
          return values[mid][0]
        # Adjust low if its too small
      elif values[mid][1] <= timestamp:
        #Set result in case we can't find the value
        res = values[mid][0] 
        low = mid + 1
      #Adjust high if its too large
      else:
        high = mid - 1 
    return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)