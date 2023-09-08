class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if  len(strs)==1:
            return [strs]
        output={}
        for i in strs:
            sortedString=''.join(sorted(i))
            if sortedString in output.keys():
                output[sortedString].append(i)
            else:
                output[sortedString]=[i]

        return output.values()