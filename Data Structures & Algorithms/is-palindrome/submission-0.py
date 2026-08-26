class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Creates two pointers, each starting from opposite ends
        left, right = 0, len(s) - 1

        while left < right:
            # Skips non-alphanumeric characters from the left
            while left < right and not self.alphaNum(s[left]):
                left += 1
            # Skips non-alphanumeric characters from the right
            while left < right and not self.alphaNum(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True
    
    def alphaNum (self, c):
        return (ord('A') <= ord(c) <=ord('Z') or
         ord('a') <= ord(c) <=ord('z') or
         ord('0') <= ord(c) <=ord('9'))
