class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isValid(d1, d):
            for i in d:
                if i not in d1:
                    return False
                elif d1[i] < d[i]:
                    return False
            return True       

        m = len(s)
        n = len(t)
        if m < n:
            return ""
        
        d = {}
        for ch in t:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1

        temp1 = []
        temp2 = []
        for i in range(m):
            if s[i] in t:
                temp1.append(i)
                temp2.append(s[i])
        if len(temp1) == 0:
            return ""
        for i in d:
            if temp2.count(i) < d[i]:
                return ""
            
        minLength = m
        l = 0
        r = m-1
        d1 = {}
        left = 0
        right = 0
        while right < len(temp1):
            if s[temp1[right]] not in d1:
                d1[s[temp1[right]]] = 1
            else:
                d1[s[temp1[right]]] += 1
            if isValid(d1, d):
                length = temp1[right] - temp1[left] + 1
                if length < minLength:
                    minLength = length
                    l = temp1[left]
                    r = temp1[right]
                while isValid(d1, d):
                    length = temp1[right] - temp1[left] + 1
                    if length < minLength:
                        minLength = length
                        l = temp1[left]
                        r = temp1[right]
                    d1[s[temp1[left]]] -= 1
                    left += 1
            right += 1
            
        return s[l:r+1] 
  