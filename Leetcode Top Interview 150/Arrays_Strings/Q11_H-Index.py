class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        ans = 0
        for i in range(n):
            if n-i >= citations[i]:
                ans = max(ans, citations[i])
            else:
                ans = max(ans, n-i)
        return ans