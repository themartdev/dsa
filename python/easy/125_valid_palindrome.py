def to_alphanum_lower(s: str):
    alnum_chars = []
    for char in s:
        if char.isalnum():
            alnum_chars.append(char)
    return ''.join(alnum_chars).lower()


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = to_alphanum_lower(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
