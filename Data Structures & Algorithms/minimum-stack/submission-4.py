class MinStack:

    def __init__(self):
        self.stack = []
        self.small = float("inf")
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:

            self.small = min(val,self.stack[-1][1])
            self.stack.append((val,self.small))

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
