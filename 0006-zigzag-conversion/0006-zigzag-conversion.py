class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        result=""
        charMap=defaultdict(list)
        index=0
        row=0

        while True:
            while row<numRows and index<len(s):
                charMap[row].append(s[index])
                row+=1
                index+=1
            row-=2
            while row>=0 and index<len(s):
                charMap[row].append(s[index])
                row-=1
                index+=1
            if index>=len(s):
                break
            row+=2

        for i in list(charMap.values()):
            rowString="".join(i)
            result=result+rowString
        return result