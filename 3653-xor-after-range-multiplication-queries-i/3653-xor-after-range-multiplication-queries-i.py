class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        for query in queries:
            idx = query[0]
            while idx <= query[1]:
                nums[idx] = (nums[idx] * query[3]) % mod
                idx += query[2]
        res = 0
        for x in nums:
            res ^= x

        return res