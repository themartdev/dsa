class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        uncommon = set()
        common = set()

        for item in s1.split(" ") + s2.split(" "):
            if item in common:
                continue
            elif item in uncommon:
                uncommon.remove(item)
                common.add(item)
            else:
                uncommon.add(item)

        return list(uncommon)
