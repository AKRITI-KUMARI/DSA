class Solution:
    def calculate(self, s: str) -> int:
        curr = 0
        ans = 0
        sign = 1
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                curr = int(s[i])
                while i+1 < len(s) and s[i+1].isdigit():
                    i += 1
                    curr = curr*10 + int(s[i])
                ans += sign * curr
                curr = 0
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
            elif s[i] == ')':
                prev = stack.pop()
                next = stack.pop()
                ans = next + ans*prev
            i += 1
        return ans