class Solution:
    def tribonacci(self, n: int) -> int:
        d = [0 for _ in range(max(n + 1, 3))]
        d[0] = 0
        d[1] = 1
        d[2] = 1

        for i in range(3, n + 1):
            d[i] = d[i - 1] + d[i - 2] + d[i - 3]

        return d[n]
