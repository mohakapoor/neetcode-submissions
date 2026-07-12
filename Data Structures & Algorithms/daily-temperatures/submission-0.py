class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            j = i+1
            found_day = False
            while j<len(temperatures) :
                if temperatures[j]>temperatures[i]:
                    res.append(j-i)
                    found_day = True
                    break
                j+=1
            if not found_day:res.append(0)
        

        return res
