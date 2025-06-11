class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_value = 0
        for num in candies:
            max_value = max(max_value, num)

        out = []
        for num in candies:
            if num + extraCandies >= max_value:
                out.append(True)
            else:
                out.append(False)
        return out
