class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = res = max_frequency = 0

        for right in range(len(s)):
            char = s[right]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
            max_frequency = max(max_frequency, count[char])
            n_replacements = right - left + 1 - max_frequency
            if n_replacements > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res
