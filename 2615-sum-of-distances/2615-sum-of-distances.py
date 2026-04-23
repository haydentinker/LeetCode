from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        mp = defaultdict(list)
        for i, num in enumerate(nums):
            mp[num].append(i)

        for positions in mp.values():
            k = len(positions)
            
            prefix = [0] * k
            prefix[0] = positions[0]
            for i in range(1, k): 
                prefix[i] = prefix[i - 1] + positions[i]
            
            for i in range(k):
                curr = positions[i]
                
                if i > 0:
                    left = curr * i - prefix[i - 1]
                else:
                    left = 0
                
                if i < k - 1:
                    right = (prefix[k - 1] - prefix[i]) - curr * (k - i - 1)
                else:
                    right = 0
                
                res[curr] = left + right
        
        return res
        