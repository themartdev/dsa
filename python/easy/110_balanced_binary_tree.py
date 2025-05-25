from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.is_balanced_rec(root)[0]

    def is_balanced_rec(self, root: Optional[TreeNode]) -> (bool, int):
        if root is None:
            return True, 0
        flag_l, depth_l = self.is_balanced_rec(root.left)
        flag_r, depth_r = self.is_balanced_rec(root.right)
        if not flag_l or not flag_r:
            return False, -1
        if abs(depth_l - depth_r) > 1:
            return False, -1
        return True, max(depth_l, depth_r) + 1
