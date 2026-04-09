from collections import defaultdict
def modinv(x):
    return 
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        b = len(nums) ** 0.25 + 1
        buckets = defaultdict(list)

        for l, r, k, v in queries:
            if k <= b: # use the expensive fast calculations for large sets
                buckets[(k, l % k)].append((l, r, v)) 
            else: # use slower for smaller sets
                idx = l
                while idx <= r:
                    nums[idx] = (nums[idx] * v) % mod
                    idx += k
        
        for (k, remainder), bucket_queries in buckets.items():
            bucket = []
            idx = remainder
            while idx < n: # append all the needed nums for the queries 
                bucket.append(nums[idx])
                idx += k

            diff = [1] * (len(bucket) + 1)

            for l, r, v in bucket_queries: #build the difference array for this bucket
                L = (l - remainder) // k
                R = (r - remainder) // k
                diff[L] = (diff[L] * v) % mod
                if R + 1 < len(diff):
                    diff[R + 1] = (diff[R + 1] * pow(v, mod - 2, mod))% mod
            running = 1
            for i in range(len(bucket)): #get the product and write back to nums
                running = (running * diff[i]) % mod
                bucket[i] = (bucket[i] * running) % mod
                nums[remainder + i * k] = bucket[i]

        res = 0
        for x in nums: #xor everything
            res ^= x
        return res