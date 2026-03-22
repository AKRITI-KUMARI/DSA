class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split()
        list2 = list1[::-1]
        return " ".join(list2)
        