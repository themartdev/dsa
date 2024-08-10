package main

func hasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}
	return hasPathSumRec(root, targetSum)
}

func hasPathSumRec(root *TreeNode, targetSum int) bool {
	if root == nil {
		return targetSum == 0
	}
	if hasPathSum(root.Left, targetSum-root.Val) {
		return true
	}
	return hasPathSum(root.Right, targetSum-root.Val)
}
