class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        index=len(digits)-1
        while carry and index>=0:
            digits[index]+=carry
            if digits[index]>=10:
                print(digits[index]%10)
                digits[index]=digits[index]%10
                carry=1
                if index==0:
                    digits.insert(0,1)
                    break
            else:
                carry=0
            index-=1
        return digits        

