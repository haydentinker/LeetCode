class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        trees = {}
        res = 0 
        left = 0 
        for right in range(len(fruits)):
            trees[fruits[right]] = trees.get(fruits[right], 0 ) + 1
          
            while len(trees.keys()) > 2:
                trees[fruits[left]] -= 1
                if not trees[fruits[left]]:
                    trees.pop(fruits[left])
                left +=1
                    
            res = max(res, (right - left +1))

        return res