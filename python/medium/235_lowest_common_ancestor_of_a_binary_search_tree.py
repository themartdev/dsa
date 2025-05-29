class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        low, high = min(p.val, q.val), max(p.val, q.val)

        curr = root
        while 1:
            if curr is None:
                raise RuntimeError("Unexpected end of tree")
            if low <= curr.val <= high:
                return curr
            elif high < curr.val:
                curr = curr.left
            elif curr.val < low:
                curr = curr.right
