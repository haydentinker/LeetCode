class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Brute Force Method
        # result=[]
        # for i in range(len(height)):
        #     for j in range(len(height)):
        #         if height[i]<height[j]:
        #             result.append((i-j)*height[i])
        #         else:
        #             result.append((i-j)*height[j])
        # result=sorted(result,reverse=True)
        # return result[0]
        highestArea=0
        right=len(height)-1
        left=0
        while(left<right):
            if height[left]>height[right]:
                highestArea=max(highestArea,((right-left)*height[right]))
                right-=1
            else:
                highestArea=max(highestArea,((right-left)*height[left]))
                left+=1
        return highestArea