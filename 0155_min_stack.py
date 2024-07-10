class MinStack:
    def __init__(self):
        self.stack =  []
        self.minimum = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minimum:
            self.mimimum = val

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        if len(self.stack):
            return self.stack[-1]


    def getMin(self) -> int:
        return self.mimimum

