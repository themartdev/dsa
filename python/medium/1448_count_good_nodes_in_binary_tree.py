class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodes_rec(root, -100000)

    def goodNodes_rec(self, root: TreeNode, max_val: int) -> int:
        if not root:
            return 0
        good = 0
        if max_val <= root.val:
            good += 1
        good += self.goodNodes_rec(root.left, max(max_val, root.val))
        good += self.goodNodes_rec(root.right, max(max_val, root.val))
        return good
