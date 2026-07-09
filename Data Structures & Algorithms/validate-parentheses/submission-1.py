class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        
        d = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for i in s:
            if i in list(d.keys()):
                if len(arr)>0 and d[i] == arr[-1]:
                    arr.pop()
                else:
                    return False
            else:
                arr.append(i)

        if len(arr) == 0:
            return True
        return False

        