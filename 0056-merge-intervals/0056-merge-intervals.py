class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:       
        intervals.sort()
        l=0
        r=1
        while r<=len(intervals)-1:
            leftInterval=intervals[l]
            rightInterval=intervals[r]
            if leftInterval[0]<=rightInterval[0] and leftInterval[1]>=rightInterval[0]:
                newInterval=[leftInterval[0],max(leftInterval[1],rightInterval[1])]
                intervals.remove(leftInterval)
                intervals[l]=newInterval
            elif rightInterval[0]<=leftInterval[0] and rightInterval[1]>=leftInterval[0]:
                newInterval=[rightInterval[0],max(leftInterval[1],rightInterval[1])]
                intervals.remove(leftInterval)
                intervals[l]=newInterval

            else:
                l+=1
                r+=1
        return intervals
