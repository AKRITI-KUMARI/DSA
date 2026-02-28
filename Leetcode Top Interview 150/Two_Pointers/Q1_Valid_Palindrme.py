class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for i in range(len(s)):
            if s[i] >= 'a' and s[i] <= 'z':
                temp += s[i]
            elif s[i] >= 'A' and s[i] <= 'Z':
                temp += chr(ord(s[i])+32)
            elif s[i] >= '0' and s[i] <= '9':
                temp += s[i]
        if temp == temp[::-1]:
            return True
        else:
            return False

      