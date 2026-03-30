class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        while i<len(path):
            if path[i] == '/':
                if i == 0:
                    stack.append('/')
                elif i != len(path)-1:
                    if len(stack) > 0 and stack[-1] != '/':
                        stack.append('/')
                i += 1
            elif path[i] == '.':
                dotCount = 1
                i += 1
                while i<len(path) and path[i] == '.':
                    dotCount += 1
                    i += 1
                if (i<len(path) and path[i] == '/') or (i == len(path)):
                    if dotCount == 2:
                        if len(stack) > 1:
                            stack.pop()
                            stack.pop()
                    if dotCount > 2:
                        s = "."*dotCount
                        stack.append(s)
                elif i < len(path) and path[i] != '/':
                    s = "."*dotCount
                    while i<len(path) and path[i] != '/':
                        s += path[i]
                        i += 1
                    stack.append(s)
            else:
                s = ""
                while i<len(path) and path[i] != '/':
                    s += path[i]
                    i += 1
                stack.append(s)
        if stack[-1] == '/' and len(stack) > 1:
            stack.pop()
        return "".join(stack)