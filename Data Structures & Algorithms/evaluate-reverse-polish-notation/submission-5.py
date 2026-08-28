class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == "+":
                a = s.pop()
                b = s.pop()
                s.append(a+b)
            elif i == "-":
                a = s.pop()
                b = s.pop()
                s.append(b-a)
            elif i == "*":
                a = s.pop()
                b = s.pop()
                s.append(b*a)
            elif i == "/":
                a = s.pop()
                b = s.pop()
                s.append(int(b/a))
            else:
                s.append(int(i))
        return s.pop()