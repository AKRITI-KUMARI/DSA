class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValidParenthesis(s):
            stack = []
            for i in s:
                if i == "(":
                    stack.append(i)
                else:
                    if len(stack) == 0:
                        return False
                    stack.pop()
            if len(stack) == 0:
                return True
            else:
                return False

        def backtrack(ans, open, close):
            if len(ans) == 2 * n:
                if isValidParenthesis(ans):
                    self.res.append(ans)
            if open > 0:
                backtrack(ans + "(", open - 1, close)
            if close > 0:
                backtrack(ans + ")", open, close - 1)

        self.res = []
        backtrack("", n, n)
        return self.res
