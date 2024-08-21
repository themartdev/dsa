from typing import Optional

from shared import Node


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        adj = {node.val: node.neighbors}
        stack = [node]
        while len(stack) > 0:
            cur = stack.pop()
            for neighbor in cur.neighbors:
                if neighbor.val not in adj:
                    adj[neighbor.val] = neighbor.neighbors
                    stack.append(neighbor)
        print(adj.keys())

        # Initialize new nodes
        new_nodes = {}
        for val in dict.keys(adj):
            new_nodes[val] = Node(val=val)

        # Build edges
        for val, prev_neighbors in adj.items():
            new_neighbors = []
            for prev in prev_neighbors:
                new_neighbors.append(new_nodes[prev.val])
            new_nodes[val].neighbors = new_neighbors

        return new_nodes[node.val]
