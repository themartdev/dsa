package medium

import "math"

func isValidBST(root *TreeNode) bool {
	if root == nil {
		return true
	}
	prev := math.MinInt
	stack := make([]*TreeNode, 0)
	for root != nil || len(stack) > 0 {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if node.Val <= prev {
			return false
		}
		prev = node.Val
		root = node.Right
	}
	return true
}
