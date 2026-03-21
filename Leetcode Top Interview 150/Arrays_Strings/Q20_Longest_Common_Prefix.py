class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        Min = strs[0]
        for word in strs:
            if len(word) < len(Min):
                Min = word
        for i in range(len(Min)):
            flag = 0
            for j in range(len(strs)):
                if Min[i] != strs[j][i]:
                    flag = 1
                    break
            if flag == 0:
                ans += Min[i]
            else:
                break
        return ans