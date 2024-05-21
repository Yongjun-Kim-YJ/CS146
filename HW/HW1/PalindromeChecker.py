import re

def isPalindrome(s: str) -> bool:
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

print(isPalindrome("ab:b,a"))
print(isPalindrome("race a car"))