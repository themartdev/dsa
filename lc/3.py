# Doing this in python to protest against the fact that go doesn't have a set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low, high = 0, 0
        _set = set()
        max_len = 0
        while high < len(s):
            if s[high] not in _set:
                _set.add(s[high])
                high += 1
            else:
                while s[high] in _set:
                    _set.remove(s[low])
                    low += 1
            max_len = max(max_len, high - low)
        return max_len
