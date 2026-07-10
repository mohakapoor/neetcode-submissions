class Solution:
    def calPoints(self, operations: List[str]) -> int:
        t = []
        final_score = 0
        for i in operations:
            if i == "+":
                score = t[-1]
                score += t[-2]
                t.append(score)
                final_score += score
            elif i == "D":
                score = 2*t[-1]
                t.append(score)
                final_score += score
            elif i == "C":
                final_score -= t.pop()
            else:
                t.append(int(i))
                final_score += int(i)
        
        return final_score