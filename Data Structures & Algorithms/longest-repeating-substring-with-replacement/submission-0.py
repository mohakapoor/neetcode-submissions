class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        left = 0
        max_len = 0
        max_freq = 0
        for right in range(len(s)):
            if s[right] not in d:
                d[s[right]] = 1
            else:
                d[s[right]] += 1

            max_freq = max(max_freq,d[s[right]])

            while (right-left+1)-max_freq >k:
                d[s[left]] -= 1
                left +=1
            
            max_len = max(max_len,right-left+1)
            

        return max_len
