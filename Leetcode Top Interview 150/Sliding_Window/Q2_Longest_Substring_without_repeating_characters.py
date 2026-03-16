class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        d = {}
        l,r = 0,0
        maxLen = 0
        while r < n:
            if s[r] in d:
                l = max(l,d[s[r]]+1)
            length = r - l + 1
            maxLen = max(maxLen,length)
            d[s[r]] = r
            r += 1
        return maxLen
  