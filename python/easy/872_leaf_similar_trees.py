from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        first, second = [], []
        self.calc_leaf_sequence(root1, first)
        self.calc_leaf_sequence(root2, second)
        if len(first) != len(second):
            return False
        for i in range(len(first)):
            if first[i] != second[i]:
                return False
        return True

    def calc_leaf_sequence(self, root: Optional[TreeNode], acc: list[int]):
        if not root:
            return
        if not root.left and not root.right:
            acc.append(root.val)
        else:
            self.calc_leaf_sequence(root.left, acc)
            self.calc_leaf_sequence(root.right, acc)
