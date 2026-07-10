class Solution:
    def calPoints(self, operations: List[str]) -> int:
        t = []
        for i in operations:
            if i == "+":
                score = t[-1]
                score += t[-2]
                t.append(score)
            elif i == "D":
                score = 2*t[-1]
                t.append(score)
            elif i == "C":
                t.pop()
            else:
                t.append(int(i))
        
        return sum(t)