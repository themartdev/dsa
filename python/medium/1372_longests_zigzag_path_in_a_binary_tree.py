from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.longestZigZag_rec(root, 0, 0)

    def longestZigZag_rec(self, root: TreeNode, left_depth: int, right_depth: int) -> int:
        max_depth = max(left_depth, right_depth)
        if root.right:
            max_depth = max(max_depth, self.longestZigZag_rec(root.right, 0, left_depth + 1))
        if root.left:
            max_depth = max(max_depth, self.longestZigZag_rec(root.left, right_depth + 1, 0))
        return max_depth
