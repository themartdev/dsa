from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            hash = ''.join(sorted(word))
            if hash in hashmap:
                hashmap[hash].append(word)
            else:
                hashmap[hash] = [word]
        output = []
        for l in hashmap.values():
            output.append(l)
        return output
