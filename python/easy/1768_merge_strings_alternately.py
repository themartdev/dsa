class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        out = []
        while i < len(word1) and i < len(word2):
            out.append(word1[i])
            out.append(word2[i])
            i += 1
        while i < len(word1):
            out.append(word1[i])
            i += 1
        while i < len(word2):
            out.append(word2[i])
            i += 1
        return "".join(out)

