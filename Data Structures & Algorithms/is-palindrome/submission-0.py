class Solution:
    def isPalindrome(self, s: str) -> bool:
        out = []
        for a in s:
            if a.isalnum():
                out.append(a.lower())
        return out == out[::-1]