class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        List1 = s.split()
        return len(List1[-1])