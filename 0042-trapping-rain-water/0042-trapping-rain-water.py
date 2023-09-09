class Solution:
    def trap(self, height: List[int]) -> int:
        waterTrapped=0
        right=len(height)-1
        left=0
        leftMax=height[0]
        rightMax=height[-1]
        while(left<=right):
            if height[left]>leftMax:
                leftMax=height[left]
            if height[right]>rightMax:
                rightMax=height[right]
            if leftMax<=rightMax:
                waterTrapped+=leftMax-height[left]
                left+=1
            else:
                waterTrapped+=rightMax-height[right]
                right-=1

        return waterTrapped