class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        bank = {}
        for char in s1:
            if char in bank:
                bank[char] += 1
            else:
                bank[char] = 1

        window_size = 0
        for right in range(len(s2)):
            char = s2[right]
            while window_size > 0 and (char not in bank or bank[char] == 0):
                bank[s2[right - window_size]] += 1
                window_size -= 1
            if char in bank and bank[char] > 0:
                bank[char] -= 1
                window_size += 1
            if window_size == len(s1):
                return True
        return False

