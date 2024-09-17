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
        res = []

        def backtrack(remaining: str, curr: str):
            if len(remaining) < 1:
                res.append(curr)
                return

            digit = remaining[0]
            newDigits = remaining[1:]

            for nextLetter in self.letters_for_digit[digit]:
                backtrack(newDigits, curr + nextLetter)

        if digits:
            backtrack(digits, "")

        return res
