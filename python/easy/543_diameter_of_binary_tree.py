from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, diameter = self.diameter_rec(root)
        return diameter

    def diameter_rec(self, root: Optional[TreeNode]) -> (int, int):
        if root is None:
            return 0, 0

        left_depth, left_diameter = self.diameter_rec(root.left)
        right_depth, right_diameter = self.diameter_rec(root.right)
        depth = max(left_depth, right_depth) + 1
        diameter = max(left_diameter, right_diameter, left_depth + right_depth)
        return depth, diameter
