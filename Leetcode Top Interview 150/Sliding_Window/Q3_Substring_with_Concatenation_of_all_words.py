class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words[0])
        windowSize = len(words)*n
        ans = []
        d = {}
        for i in words:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        def validConcat(s1):
            for i in d:
                count = d[i]
                for j in range(0, len(s1), n):
                    if s1[j:j+n] == i:
                        count -= 1
                        if count == 0:
                            break
                if count != 0:
                    return False
            return True

        
        for i in range(len(s)-windowSize+1):
            window = s[i:i+windowSize]
            if validConcat(window):
                ans.append(i)
        return ans