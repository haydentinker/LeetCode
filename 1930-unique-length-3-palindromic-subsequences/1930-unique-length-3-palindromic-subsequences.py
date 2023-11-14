class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result=0
        #Get unique chars within the string
        uniqueChars=set(s)
        #Iterate over chars
        for i in uniqueChars:
            #Look to see if it occurs twice
            left=s.find(i)
            right=s.rfind(i)
            #If they aren't the same index add the length the chars between them
            if left<right:
                result+=len(set(s[left+1:right]))
        return result
    #Brute force 
    #     self.result=set()
    #     self.s=s
    #     self.search(0,"")
    #     return len(self.result)
    # def search(self, index,curr):
    #     if len(curr)==3:
    #         if curr==curr[::-1] and curr not in self.result:
    #             self.result.add(curr)
    #     if index<len(self.s):
    #         self.search(index+1,curr)
    #         curr=curr+self.s[index]
    #         self.search(index+1,curr)
        