class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result=float('inf')
        index=0
        while index+k-1<len(blocks):
            whiteblocks=0
            for i in blocks[index:index+k]:
                if i=='W':
                    whiteblocks+=1
            result=min(whiteblocks,result)
            index+=1
        return result