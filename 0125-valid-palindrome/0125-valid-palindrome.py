class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Brute Force
        # i=0
        # j=len(s)-1
        # while(i<=j):

        #     while i<=j and not s[i].isalnum():
        #         i+=1
        #     while i<=j and not s[j].isalnum():
        #         j-=1
        #     if i<=j and not s[i].lower()==s[j].lower():
        #         return False
        #     i+=1
        #     j-=1
        # return True

        #Cleaner solution
        result=""
        for i in s:
            #If i is alphanumeric then append to result string
            if i.isalnum():
                result+=i
        #Make sure result string is lowercase
        result=result.lower()
        #If result == result backwards
        return result==result[::-1]