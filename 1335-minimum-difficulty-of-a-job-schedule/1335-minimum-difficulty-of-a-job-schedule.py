class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d>len(jobDifficulty):
            return -1

        cache={}
        def search (index,daysLeft,curr_max):
            if index== len(jobDifficulty):
                return 0 if daysLeft==0 else float("inf")
            if daysLeft==0:
                return float("inf")
            if (index,daysLeft,curr_max) in cache:
                return cache[(index,daysLeft,curr_max)]
            curr_max=max(curr_max,jobDifficulty[index])
            res=min(
            search(index+1,daysLeft,curr_max), #continue
            curr_max+search(index+1,daysLeft-1,-1) #end
            )
            cache[(index,daysLeft,curr_max)]=res
            return res
        return search(0,d,-1)