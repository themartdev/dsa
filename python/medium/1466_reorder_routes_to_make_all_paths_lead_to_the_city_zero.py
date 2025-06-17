class Solution:
    def compress(self, chars: list[str]) -> int:
        groups = []
        curr, n = None, 0
        for char in chars:
            if char != curr:
                if curr:
                    groups.append(curr * n)
                curr = char
                n = 1
            else:
                n += 1
        if curr:
            groups.append(curr * n)

        i = 0
        for group in groups:
            if len(group) == 1:
                chars[i] = group
                i += 1
            else:
                val = f"{group[0]}{len(group)}"
                for char in val:
                    chars[i] = char
                    i += 1
        return i
