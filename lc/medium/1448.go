package medium

import "math"

func goodNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}

	return goodNodesRec(root, math.MinInt)
}

func goodNodesRec(root *TreeNode, maxVal int) int {
	if root == nil {
		return 0
	}
	total := 0
	if root.Val >= maxVal {
		maxVal = root.Val
		total++
	}
	total += goodNodesRec(root.Left, maxVal) + goodNodesRec(root.Right, maxVal)
	return total
}
