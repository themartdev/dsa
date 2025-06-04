class Solution:
    letters_for_digit = {
        "2": ("a", "b", "c"),
        "3": ("d", "e", "f"),
        "4": ("g", "h", "i"),
        "5": ("j", "k", "l"),
        "6": ("m", "n", "o"),
        "7": ("p", "q", "r", "s"),
        "8": ("t", "u", "v"),
        "9": ("w", "x", "y", "z"),
    }

    def letterCombinations(self, digits: str) -> list[str]:
        out = []

        if not digits:
            return []

        def backtrack(trace: str, idx: int):
            if idx > len(digits) - 1:
                out.append(trace)
                return

            for letter in self.letters_for_digit[digits[idx]]:
                backtrack(trace + letter, idx + 1)

        backtrack("", 0)

        return out
