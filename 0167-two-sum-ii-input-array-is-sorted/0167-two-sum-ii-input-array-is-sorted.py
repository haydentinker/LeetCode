class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1 
        while right < len(numbers) and left <= right:
            pointerSum = numbers[left] + numbers[right]
            if pointerSum == target:
                return [left +1 , right +1]
            elif pointerSum > target:
                right -=1
            else:
                left+=1
        

