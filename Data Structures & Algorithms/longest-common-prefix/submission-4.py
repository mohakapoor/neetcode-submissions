class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = ""
        smol = min(strs)
        for i in range(len(smol)):
            temp = strs[0][i]
            for c in strs:
                if temp != c[i]:
                    return word
            word += temp
        return word