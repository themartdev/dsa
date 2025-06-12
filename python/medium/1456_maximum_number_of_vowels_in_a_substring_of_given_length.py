class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}

        if k == 1:
            for char in s:
                if char in vowels:
                    return 1
            return 0

        n_vowels = sum([1 if x in vowels else 0 for x in s[:k]])
        max_vowels = n_vowels
        for i in range(k, len(s)):
            if s[i] in vowels:
                n_vowels += 1
            if s[i - k] in vowels:
                n_vowels -= 1
            max_vowels = max(max_vowels, n_vowels)
        return max_vowels
