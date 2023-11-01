class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        self.res=[]
        self.curr=""
        self.digits=digits
        self.keyBoard= {
            '0': None,
            '1': None,
            "2": ['a','b','c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            '7': ["p",'q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        self.getCombos(0)
        return self.res
    def getCombos(self,index):
        if index==len(self.digits):
            self.res.append(self.curr)
            return
        for letters in self.keyBoard[self.digits[index]]:
            for letter in letters:
                self.curr=self.curr+(letter)
                self.getCombos(index+1)
                self.curr=self.curr[:-1]

   