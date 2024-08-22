import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for target, source in prerequisites:
            adj[source].append(target)
            in_degree[target] += 1

        q: collections.deque[int] = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for adjacent in adj[node]:
                in_degree[adjacent] -= 1
                if in_degree[adjacent] == 0:
                    q.append(adjacent)
        return result if len(result) == numCourses else []

