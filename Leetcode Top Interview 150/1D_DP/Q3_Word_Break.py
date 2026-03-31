class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)

        # one dimensional DP array for storing boolean results 
        # for each substring of s starting from index 0
        dp = [False] * (n + 1)
        dp[0] = True    # Empty string is always valid

        for i in range(1, n + 1):
            for j in range(i):
                # check previous word : s[:j] through dp[j]
                # check next word : s[j:i]
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[n]
        