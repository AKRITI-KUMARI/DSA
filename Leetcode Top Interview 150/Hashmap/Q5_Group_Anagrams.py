class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            temp = "".join(sorted(i))
            if temp not in d:
                d[temp] = [i]
            else:
                d[temp].append(i)
        ans = []
        for i in d:
            ans.append(d[i])
        return ans