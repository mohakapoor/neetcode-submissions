class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 0
            d[i] +=1
        for i in t:
            if i not in d:
                return False
            d[i] -=1
        
        return all(a==0 for a in d.values())