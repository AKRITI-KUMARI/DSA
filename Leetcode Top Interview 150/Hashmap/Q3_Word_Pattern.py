class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = list(s.split())
        if len(l) != len(pattern):
            return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if l[i] in d.values():
                    return False
                d[pattern[i]] = l[i]
            else:
                if d[pattern[i]] != l[i]:
                    return False
        return True