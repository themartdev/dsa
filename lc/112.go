package main

import "github.com/simon-martineau/dsa/lc/ds"

func main() {
}

func hasPathSum(root *ds.TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}
	return hasPathSumRec(root, targetSum)
}

func hasPathSumRec(root *ds.TreeNode, targetSum int) bool {
	if root == nil {
		return targetSum == 0
	}
	if hasPathSum(root.Left, targetSum-root.Val) {
		return true
	}
	return hasPathSum(root.Right, targetSum-root.Val)
}
