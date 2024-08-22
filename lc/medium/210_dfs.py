class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj: list[list[int]] = [[] for _ in range(numCourses)]
        for course, req in prerequisites:
            adj[course].append(req)

        # 0: not visited, 1: finished, 2: visiting
        visited = [0 for _ in range(numCourses)]
        res = []

        def dfs(node: int) -> bool:
            if visited[node] == 2:
                return False
            elif visited[node] == 1:
                return True
            visited[node] = 2
            for neighbor in adj[node]:
                if visited[neighbor] != 1:
                    if not dfs(neighbor):
                        return False
            visited[node] = 1
            res.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
