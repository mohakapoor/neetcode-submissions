class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            key = "".join(sorted(i))
            if d.get(key,0) == 0:
                d[key] = []
            d[key].append(i)
        return list(d.values())