class MinStack:

    def __init__(self):
        self.stack = []
        self.Min = float('inf')

    def push(self, val: int) -> None:
        if val <= self.Min:
            self.stack.append(self.Min)
            self.Min = min(val, self.Min)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.Min:
            self.Min = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()