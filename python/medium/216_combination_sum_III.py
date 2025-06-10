class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        out: list[list[int]] = []

        def dfs(trace: list[int], min_val: int, remaining: int):
            if remaining == 0 and len(trace) == k:
                out.append(trace)
                return
            if len(trace) == k or remaining < 0:
                return
            for i in range(min_val, 10):
                dfs(trace + [i], i + 1, remaining - i)

        dfs([], 1, n)

        return out
