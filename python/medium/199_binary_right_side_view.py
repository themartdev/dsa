from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        self.rightSideView_rec(root, 0, view)
        return view

    def rightSideView_rec(self, root: Optional[TreeNode], depth: int, view: list[int]):
        if not root:
            return

        if len(view) == depth:
            view.append(root.val)

        self.rightSideView_rec(root.right, depth + 1, view)
        self.rightSideView_rec(root.left, depth + 1, view)
