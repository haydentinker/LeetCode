class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def isNice(s):
            return len(set(s.lower())) == (len(set(s)) // 2)

        window=len(s)

        while window:
            for i in range(len(s)-window+1):
                substring=s[i:i+window]
                if isNice(substring):
                    return substring
            window-=1
        return ''
            
            