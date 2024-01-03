class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result=0
        prev=0
        for i in bank:
            cur=i.count("1")
            if cur==0:
                continue
            result+=prev*cur
            prev=cur
        return result
        