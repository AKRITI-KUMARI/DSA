class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for i in ransomNote:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
    
        for i in d:
            if magazine.count(i) < d[i]:
                return False
        return True