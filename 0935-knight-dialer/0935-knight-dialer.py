class Solution:
    def knightDialer(self, n: int) -> int:
        mapping = {
            0:[6,4],
            1:[6,8],
            2:[9,7],
            3:[4,8],
            4:[0,9,3],
            5:[],
            6:[0,7,1],
            7:[6,2],
            8:[3,1],
            9:[4,2]
        }
        mod=1e9+7
        @cache
        def search(num,jumps):
            if jumps==0:
                return 1
            result=0
            for i in mapping[num]:
                result=(result+search(i,jumps-1))%mod
            return result
        result=0
        for i in range(10):
            result=(result+search(i,n-1))%mod
        return int(result)