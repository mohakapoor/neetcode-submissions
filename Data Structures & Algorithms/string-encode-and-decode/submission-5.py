class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []

        for s in strs:
            parts.append(str(len(s)))
            parts.append(",")
            parts.append(s)

        return "".join(parts)
    def decode(self, s: str) -> List[str]:
        i = 0 
        strs = []
        while i<len(s):
            j = i
            while s[j] != ",":
                j+=1
            length = int(s[i:j])
            strs.append(s[j+1:j+1+length])
            i = j+1+length

        return strs

