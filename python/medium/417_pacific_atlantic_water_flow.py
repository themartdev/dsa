from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        # solve pacific
        visited_p = [[0 for _ in range(n)] for _ in range(m)]
        start_p = set([(0, j) for j in range(n)] + [(i, 0) for i in range(m)])
        self.flow_up(heights, visited_p, list(start_p))

        # solve atlantic
        visited_a = [[0 for _ in range(n)] for _ in range(m)]
        start_a = set([(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m)])
        self.flow_up(heights, visited_a, list(start_a))

        ans = []
        for i in range(m):
            for j in range(n):
                if visited_p[i][j] and visited_a[i][j]:
                    ans.append([i, j])
        return ans

    def flow_up(self, heights: list[list[int]], visited: list[list[int]], start: list[(int, int)]):
        print(start)
        q = list(start)
        for i, j in q:
            visited[i][j] = 1

        while q:
            i, j = q.pop()
            for ia, ja in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= ia < len(heights) and 0 <= ja < len(heights[0]) and not visited[ia][ja] and heights[i][j] <= \
                        heights[ia][ja]:
                    visited[ia][ja] = 1
                    q.append((ia, ja))


if __name__ == "__main__":
    ans = Solution().pacificAtlantic([[1, 1], [1, 1], [1, 1]])
    print(f"answer: {ans}")
