from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        self.levelOrder_rec(root, 0, out)
        return out

    def levelOrder_rec(self, root: Optional[TreeNode], depth: int, out: list[list[int]]):
        if not root:
            return
        if len(out) == depth:
            out.append([])

        out[depth].append(root.val)
        self.levelOrder_rec(root.left, depth + 1, out)
        self.levelOrder_rec(root.right, depth + 1, out)
