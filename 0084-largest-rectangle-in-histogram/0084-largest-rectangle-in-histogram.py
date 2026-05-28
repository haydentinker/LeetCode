class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0 
        for index, height in enumerate(heights):
            startOfRect = index
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                res = max(res, h*(index-idx) )
                startOfRect = idx
            stack.append((startOfRect, height))
        for i, h in stack:
            res = max(res, h*(len(heights)-i))

        return res