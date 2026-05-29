class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""
        length = len(min(strs,key=len))
        for i in range(length):
            check = strs[0][i]
            for j in strs:
                 if check != j[i]:
                    return out
            out += check
        return out