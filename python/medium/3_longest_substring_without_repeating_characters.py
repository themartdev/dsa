class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        pool = set()
        left = 0
        for right in range(len(s)):
            char = s[right]
            while char in pool and left < right:
                pool.remove(s[left])
                left += 1
            pool.add(char)
            max_len = max(len(pool), max_len)

        return max_len
