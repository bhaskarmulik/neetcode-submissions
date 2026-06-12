class MinStack:

    def __init__(self):
        self.l = list()
        self.minval = None

    def push(self, val: int) -> None:
        if not self.l:
            self.minval = val
        else:
            self.minval= val if val < self.minval else self.minval
        self.l.append((val, self.minval))

    def pop(self) -> None:
        print(f"Before popping : {self.l}")
        self.l.pop()
        self.minval = self.l[-1][1] if self.l else None
        print(f"After popping : {self.l}")

    def top(self) -> int:
        return self.l[-1][0]

    def getMin(self) -> int:
        return self.l[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()