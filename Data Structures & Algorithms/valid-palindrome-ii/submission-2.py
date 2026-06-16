class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left,right):
            while left<right:
                if s[left] !=s[right]: return False
                left +=1
                right -= 1
            return True
        right = len(s)-1
        for left in range(len(s)):
            if s[left] != s[right]:
                return(isPalindrome(left+1,right) or isPalindrome(left,right-1))
            else:
                right -= 1
        return True