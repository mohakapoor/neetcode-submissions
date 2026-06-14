class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        max_len = 0
        left = 0
        for right in range(len(s)):
            print("before",temp,right)
            while s[right] in temp:
                temp.remove(s[left])
                left+=1
            temp.add(s[right])
            print("after",temp,right)

            max_len = max(max_len,len(temp))
        return max_len