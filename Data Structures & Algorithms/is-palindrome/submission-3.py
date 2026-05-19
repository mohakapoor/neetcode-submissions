class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        for i in range(len(s)//2):
            if not s[left].isalnum():
                left += 1
            if not s[right].isalnum():
                right -=1
            if s[left].isalnum() and s[right].isalnum():
                print(f"left = {s[left].lower()} right = {s[right].lower()}")
                if not s[left].lower() == s[right].lower(): return False
                left += 1 
                right -= 1
            
        return True