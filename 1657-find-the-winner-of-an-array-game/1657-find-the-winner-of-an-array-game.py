class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        consecutiveWinner=[0,0]
        if k>len(arr):
            return max(arr)
        while consecutiveWinner[1] <k:
            if arr[0]>arr[1]:
                if consecutiveWinner[0]==arr[0]:
                    consecutiveWinner[1]+=1
                else:
                    consecutiveWinner[0]=arr[0]
                    consecutiveWinner[1]=1
                moveEle=arr.pop(1)
                arr.append(moveEle)
            else:
                if consecutiveWinner[0]==arr[1]:
                    consecutiveWinner[1]+=1
                else:
                    consecutiveWinner[0]=arr[1]
                    consecutiveWinner[1]=1
                moveEle=arr.pop(0)
                arr.append(moveEle)
        return consecutiveWinner[0]