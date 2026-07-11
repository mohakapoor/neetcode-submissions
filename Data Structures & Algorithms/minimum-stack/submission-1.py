class MinStack:

    def __init__(self):
        self.s1 = []
    def push(self, val: int) -> None:
        if self.s1:

            get_small = min(val,self.s1[-1][1])
        else:
            get_small = val
        self.s1.append([val,get_small])
        

    def pop(self) -> None:
        self.s1.pop()

        

    def top(self) -> int:
        
        return self.s1[-1][0]
        

    def getMin(self) -> int:
        return self.s1[-1][1]
        
