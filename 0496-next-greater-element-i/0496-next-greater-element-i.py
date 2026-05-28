class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreaterElement = {}

        for index, value in enumerate(nums2):
            while stack and value > nums2[stack[-1]]:
                idx = stack.pop()
                nextGreaterElement[nums2[idx]] = value
            stack.append(index)
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in nextGreaterElement:
                res[i] = nextGreaterElement[nums1[i]]
        return res