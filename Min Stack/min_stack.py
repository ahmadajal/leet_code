class MinStack:

    def __init__(self):
        self.min = (2**31)-1
        self.min_at_index = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(val, self.min)
        self.min_at_index.append(self.min)
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_at_index.pop()
        self.min = self.min_at_index[-1] if self.min_at_index else (2**31)-1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min